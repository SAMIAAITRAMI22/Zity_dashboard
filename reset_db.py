import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(
    host     = "localhost",
    port     = 5432,
    user     = "postgres",
    password = "admin123"
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

try:
    # ── Ferme toutes les connexions actives ───────────────
    cursor.execute("""
        SELECT pg_terminate_backend(pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE pg_stat_activity.datname = 'zity_db'
        AND pid <> pg_backend_pid();
    """)
    print("✓ Connexions fermées")

    # ── Supprime et recrée ────────────────────────────────
    cursor.execute("DROP DATABASE IF EXISTS zity_db;")
    print("✓ Base supprimée")

    cursor.execute("CREATE DATABASE zity_db;")
    print("✓ Base recréée")

except Exception as e:
    print(f"Erreur : {e}")
finally:
    cursor.close()
    conn.close()