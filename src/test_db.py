# Archivo de prueba para validar la conexión a la base de datos
# Este script intenta conectar a la base de datos usando la configuración de database.py
# y ejecuta una consulta simple para verificar que la conexión funciona.

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from infraestructure.database import engine, SessionLocal
from sqlalchemy import text

def test_db_connection():
    try:
        # Intentar crear una sesión
        db = SessionLocal()
        # Ejecutar una consulta simple para probar la conexión
        result = db.execute(text("SELECT 1")).fetchone()
        if result:
            print("✅ Conexión a la base de datos exitosa.")
            print(f"Resultado de la consulta de prueba: {result}")
        else:
            print("❌ La consulta de prueba no devolvió resultados.")
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