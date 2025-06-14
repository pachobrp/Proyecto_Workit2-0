from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp

app = Flask(__name__)
CORS(app)

# Registrar rutas
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return {'message': 'API de Work.it funcionando'}

if __name__ == '__main__':
    print("🔌 Servidor Flask ejecutándose en http://localhost:3001")
    app.run(port=3001, debug=True)
