import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal, engine, Base

# Import de TOUS les modèles pour créer les tables
from app.models.user       import User
from app.models.product    import Product
from app.models.sales      import Sale
from app.models.prediction import Prediction

from app.utils.security import hash_password

# Crée toutes les tables
print("Création des tables...")
Base.metadata.create_all(bind=engine)
print("Tables créées !")

# Crée l'admin
db = SessionLocal()

existing = db.query(User).filter(User.email == "admin@gmail.com").first()

if not existing:
    admin = User(
        name     = "Admin Zity",
        email    = "admin@gmail.com",
        password = hash_password("admin123"),
        role     = "admin"
    )
    db.add(admin)
    db.commit()
    print("Admin créé avec succès !")
    print("Email    : admin@gmail.com")
    print("Password : admin123")
else:
    print("Admin existe déjà.")
# Ajoute après la création de l'admin
analyste_exist = db.query(User).filter(User.email == "analyste@gmail.com").first()
if not analyste_exist:
    analyste = User(
        name     = "Analyste Zity",
        email    = "analyste@gmail.com",
        password = hash_password("analyste123"),
        role     = "analyste"
    )
    db.add(analyste)
    db.commit()
    print("Analyste créé : analyste@gmail.com / analyste123")
db.close()