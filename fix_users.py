from app.database import SessionLocal
from app.models.user import User

db = SessionLocal()

users = db.query(User).all()

if not users:
    print("Aucun utilisateur trouvé en base.")
else:
    for u in users:
        u.is_active = True
        print(f"Activé : {u.email} | role={u.role}")
    db.commit()
    print("Tous les comptes sont maintenant actifs !")

db.close()