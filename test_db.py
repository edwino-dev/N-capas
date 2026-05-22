# Archivo de prueba para validar la conexión a la base de datos
# Este script intenta conectar a la base de datos usando la configuración de database.py
# y ejecuta una consulta simple para verificar que la conexión funciona.

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))
from infraestructure.database import engine, SessionLocal, DATABASE_URL
from sqlalchemy import text

def test_db_connection():
    try:
        # Intentar crear una sesión
        db = SessionLocal()
        # Ejecutar una consulta breve: SELECT * FROM roles LIMIT 5
        result = db.execute(text("SELECT * FROM ROLES LIMIT 5")).fetchall()
        if result:
            print("✅ Conexión a la base de datos exitosa.")
            print("Resultado de la consulta SELECT * FROM roles (limitado a 5 filas):")
            for row in result:
                print(row)
        else:
            print("❌ La consulta no devolvió resultados.")
        db.close()
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return False
    return True

if __name__ == "__main__":
    print("Iniciando prueba de conexión a la base de datos...")
    success = test_db_connection()
    if success:
        print("Prueba completada exitosamente.")
    else:
        print("Prueba fallida. Verifica la configuración de la base de datos.")