from flask import Flask, render_template

# Fichero para inicializar componentes, instacias, temporizadores
# Se inicia una instancia de Flask
app = Flask(__name__)

# Importar routes
from app import routes

#Importar referenciales
from app.routes.referenciales.sala.sala_routes import sal

#Registro de paquetes
modulo_referencial = "/referencial"
app.register_blueprint(sal, url_prefix=f"{modulo_referencial}/sala")

app.secret_key = "123"