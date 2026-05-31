import numpy as np
import sys
sys.path.append('.')

from app.database import SessionLocal
from app.services.prediction import prepare_data, train_and_predict, predict_top_products

db = SessionLocal()

print("=" * 60)
print("TEST DE VALIDITÉ DU MODÈLE ML — ZITY DASHBOARD")
print("=" * 60)

# ── TEST 1 : Données disponibles ───────────────────────────
print("\n[TEST 1] Données disponibles en base...")
df, last_period, nb_months = prepare_data(db)

if df is None:
    print("ÉCHEC — Aucune donnée. Importez un CSV d'abord.")
    db.close()
    exit()

print(f"OK — {nb_months} mois de données trouvés")
print(f"     Période : {df['year'].min():.0f}-{df['month'].min():02.0f}"
      f" → {df['year'].max():.0f}-{df['month'].max():02.0f}")
print(f"     Revenus min  : {df['revenue'].min():,.2f} MAD")
print(f"     Revenus max  : {df['revenue'].max():,.2f} MAD")
print(f"     Revenus moy  : {df['revenue'].mean():,.2f} MAD")

# ── TEST 2 : Régression manuelle ────────────────────────────
print("\n[TEST 2] Régression linéaire manuelle...")

X = df["index"].values
y = df["revenue"].values

x_mean = np.mean(X)
y_mean = np.mean(y)
num    = np.sum((X - x_mean) * (y - y_mean))
den    = np.sum((X - x_mean) ** 2)

if abs(den) < 1e-10:
    print("ATTENTION — Données identiques, pente = 0")
    pente, intercept = 0.0, y_mean
else:
    pente     = num / den
    intercept = y_mean - pente * x_mean

print(f"OK — Pente     : {pente:+.2f} MAD/mois")
print(f"     Intercept  : {intercept:.2f} MAD")

if pente > 0:
    print(f"     Tendance   : HAUSSE (+{pente:.2f} MAD par mois)")
elif pente < 0:
    print(f"     Tendance   : BAISSE ({pente:.2f} MAD par mois)")
else:
    print(f"     Tendance   : STABLE")

# ── TEST 3 : Score R² ────────────────────────────────────────
print("\n[TEST 3] Calcul Score R²...")

y_pred = pente * X + intercept
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)

if ss_tot < 1e-10:
    r2_raw = 1.0
    print("ATTENTION — SS_tot ≈ 0 (données trop uniformes)")
else:
    r2_raw = 1.0 - (ss_res / ss_tot)

print(f"OK — R² brut   : {r2_raw * 100:.1f}%")
print(f"     SS_res     : {ss_res:,.2f}")
print(f"     SS_tot     : {ss_tot:,.2f}")

if r2_raw < 0:
    print("     VERDICT : Modèle moins bon que la moyenne (normal avec peu de données)")
elif r2_raw < 0.3:
    print("     VERDICT : Faible corrélation")
elif r2_raw < 0.6:
    print("     VERDICT : Corrélation moyenne")
elif r2_raw < 0.8:
    print("     VERDICT : Bonne corrélation")
else:
    print("     VERDICT : Très forte corrélation")

# ── TEST 4 : Prédiction cohérente ───────────────────────────
print("\n[TEST 4] Cohérence des prédictions...")

result = train_and_predict(db)

if not result["success"]:
    print(f"ÉCHEC — {result['error']}")
else:
    rev_predit = result["next_revenue"]
    rev_moy    = result["avg_rev"]
    ratio      = rev_predit / rev_moy if rev_moy > 0 else 0

    print(f"OK — Mois prédit  : {result['next_month']}")
    print(f"     Revenu prédit : {rev_predit:,.2f} MAD")
    print(f"     Revenu moyen  : {rev_moy:,.2f} MAD")
    print(f"     Ratio prédit/moy : {ratio:.2f}x")

    if 0.3 <= ratio <= 3.0:
        print(f"     Cohérence     : OK (dans les limites réalistes 0.3x à 3x)")
    else:
        print(f"     Cohérence     : HORS LIMITES — vérifiez les données")

    print(f"     Score R²      : {result['score_rev']}%")
    print(f"     Qualité       : {result['qualite']}")
    print(f"     MAE           : {result['mae']:,.2f} MAD")

# ── TEST 5 : Prédictions produits ───────────────────────────
print("\n[TEST 5] Prédictions par produit...")

products = predict_top_products(db)

if not products:
    print("ÉCHEC — Aucun produit trouvé")
else:
    print(f"OK — {len(products)} produits analysés")
    for i, p in enumerate(products[:3], 1):
        print(f"     {i}. {p['name']:<25} "
              f"{p['qty']:>5} unités ({p['pct']}%) → {p['rec_type'].upper()}")

# ── TEST 6 : Stabilité sur répétitions ──────────────────────
print("\n[TEST 6] Stabilité (3 appels consécutifs)...")

resultats = []
for i in range(3):
    r = train_and_predict(db)
    if r["success"]:
        resultats.append(r["next_revenue"])

if len(resultats) == 3:
    ecart = max(resultats) - min(resultats)
    if ecart < 0.01:
        print(f"OK — Résultats stables : {resultats[0]:,.2f} MAD (écart={ecart:.4f})")
    else:
        print(f"ATTENTION — Instabilité détectée : {resultats} (écart={ecart:.2f})")
else:
    print("ÉCHEC — Impossible d'exécuter 3 fois")

# ── RÉSUMÉ ──────────────────────────────────────────────────
print("\n" + "=" * 60)
print("RÉSUMÉ")
print("=" * 60)
print(f"  Mois de données    : {nb_months}")
print(f"  Score R² final     : {result['score_rev'] if result.get('success') else 'N/A'}%")
print(f"  MAE                : {result['mae'] if result.get('success') else 'N/A'} MAD")
print(f"  Tendance           : {result['trend'].upper() if result.get('success') else 'N/A'}")
print(f"  Qualité modèle     : {result['qualite'] if result.get('success') else 'N/A'}")

if nb_months < 4:
    print("\n  CONSEIL : Importez au moins 6-12 mois de données")
    print("  pour obtenir des prédictions fiables.")
elif nb_months < 8:
    print("\n  CONSEIL : Bon début — plus de données améliorera")
    print("  encore la précision des prédictions.")
else:
    print("\n  CONSEIL : Volume de données suffisant.")
    print("  Le modèle est fiable.")

print("=" * 60)
db.close()