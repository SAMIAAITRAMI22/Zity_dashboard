from app.utils.email_sender import send_reset_code

result = send_reset_code(
    to_email  = "n'importe_quel_email@gmail.com",
    code      = "483921",
    user_name = "Samia"
)
print("Succès !" if result else "Échec")