import sqlite3

DB_NAME = "patitassanas.db"


def get_connection():
    """Crea y retorna una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def crear_base_datos():
    """
    Crea la base de datos patitassanas.db y la tabla pacientes
    si no existen todavía.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # CREATE TABLE IF NOT EXISTS evita duplicar o generar error
    # al ejecutar el script varias veces (idempotencia).
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_mascota TEXT NOT NULL,
            especie TEXT NOT NULL,
            edad INTEGER NOT NULL CHECK (edad >= 0),
            nombre_propietario TEXT NOT NULL,
            telefono_propietario TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    crear_base_datos()
    print("Base de datos y tabla 'pacientes' listas.")