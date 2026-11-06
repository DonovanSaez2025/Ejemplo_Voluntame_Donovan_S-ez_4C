# Importar la app de Flask
from flask_app import app

# Importar controladores
from flask_app.controllers.controlador_usuarios import usuarios_bp
from flask_app.controllers.controlador_misiones import misiones_bp

# Registrar de BluePrints
app.register_blueprint(usuarios_bp)
app.register_blueprint(misiones_bp)

# Debug
if __name__ == "__main__":
    app.run(debug=True)