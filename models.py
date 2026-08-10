from database import get_connection


def registrar_paciente(nombre_mascota, especie, edad, nombre_propietario, telefono_propietario):
    """
    Inserta un nuevo paciente en la tabla pacientes.

    MEDIDA DE SEGURIDAD 1 (Validación de entradas):
    Se valida que la edad no sea negativa antes de insertar el registro,
    evitando datos inconsistentes en la base de datos.
    """
    if edad is None or int(edad) < 0:
        raise ValueError("La edad debe ser un número mayor o igual a 0.")

    conn = get_connection()
    cursor = conn.cursor()

    # MEDIDA DE SEGURIDAD 2 (Consultas parametrizadas):
    # Se usan marcadores de posición (?) en lugar de concatenar texto,
    # lo que evita ataques de inyección SQL.
    cursor.execute("""
        INSERT INTO pacientes (nombre_mascota, especie, edad, nombre_propietario, telefono_propietario)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre_mascota, especie, edad, nombre_propietario, telefono_propietario))

    conn.commit()
    conn.close()


def listar_pacientes():
    """Retorna todos los pacientes registrados, ordenados por id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes ORDER BY id")
    pacientes = cursor.fetchall()
    conn.close()
    return pacientes


def eliminar_paciente(id_paciente):
    """Elimina un paciente de la base de datos según su id (consulta parametrizada)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pacientes WHERE id = ?", (id_paciente,))
    conn.commit()
    conn.close()


def actualizar_paciente(id_paciente, nombre_mascota, especie, edad, nombre_propietario, telefono_propietario):
    """(Opcional) Actualiza los datos de un paciente existente."""
    if edad is None or int(edad) < 0:
        raise ValueError("La edad debe ser un número mayor o igual a 0.")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE pacientes
        SET nombre_mascota = ?, especie = ?, edad = ?, nombre_propietario = ?, telefono_propietario = ?
        WHERE id = ?
    """, (nombre_mascota, especie, edad, nombre_propietario, telefono_propietario, id_paciente))
    conn.commit()
    conn.close()