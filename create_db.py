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
    cursor.execute("CREATE DATABASE zity_db;")
    print("✓ Base zity_db créée avec succès !")
except Exception as e:
    print(f"Info : {e}")
finally:
    cursor.close()
    conn.close()