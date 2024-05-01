# Importa la clase Flask del módulo flask
from flask import Flask
from flask import render_template

# Crea una instancia de la aplicación Flask
app = Flask(__name__, static_url_path='/static')

# Define una ruta para la página de creación de cuenta
@app.route('/')
def CrearCuenta():
    return render_template('CrearCuenta.html')

# Define una ruta para la página de inicio de sesión (método POST)
@app.route('/IniciarSesion', methods=['POST'])
def IniciarSesion():
    return render_template('IniciarSesion.html')

# Define una ruta para la página principal (método POST)
@app.route('/PaginaPrincipal', methods=['POST'])
def PaginaPrincipal():
    return render_template('PaginaPrincipal.html')