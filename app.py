from flask import Flask, render_template, request, redirect, url_for
from database import crear_base_datos
from models import registrar_paciente, listar_pacientes, eliminar_paciente

app = Flask(__name__)

# Se crea la base de datos (si no existe) al iniciar la aplicación.
crear_base_datos()


@app.route("/", methods=["GET"])
def index():
    """Muestra el formulario y la lista de pacientes registrados."""
    pacientes = listar_pacientes()
    return render_template("index.html", pacientes=pacientes)


@app.route("/registrar", methods=["POST"])
def registrar():
    """Procesa el registro de un nuevo paciente."""
    nombre_mascota = request.form.get("nombre_mascota", "").strip()
    especie = request.form.get("especie", "").strip()
    edad = request.form.get("edad", "").strip()
    nombre_propietario = request.form.get("nombre_propietario", "").strip()
    telefono_propietario = request.form.get("telefono_propietario", "").strip()

    # Validación básica de campos obligatorios antes de tocar la base de datos.
    if nombre_mascota and especie and edad.isdigit() and nombre_propietario and telefono_propietario:
        registrar_paciente(nombre_mascota, especie, int(edad), nombre_propietario, telefono_propietario)

    return redirect(url_for("index"))


@app.route("/eliminar/<int:id_paciente>", methods=["POST"])
def eliminar(id_paciente):
    """Elimina un paciente según su id."""
    eliminar_paciente(id_paciente)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)