from flask import Blueprint, request, jsonify
from db import get_connection
import sqlite3

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return {"success": False, "message": "No JSON data received"}, 400
    username = data.get('username')
    password = data.get('password')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT id, username FROM users WHERE username = ? AND password = ?',
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify(success=True, user={'id': user['id'], 'username': user['username']})
    else:
        return jsonify(success=False, message='Credenciales incorrectas'), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify(success=False, message="No se recibieron datos"), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(success=False, message="Faltan campos obligatorios"), 400

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, password)
        )
        conn.commit()
        return jsonify(success=True, message="Usuario registrado correctamente"), 201
    except sqlite3.IntegrityError:
        return jsonify(success=False, message="El nombre de usuario ya existe"), 409
    finally:
        conn.close()




# Endpoint prueba para usuarios

@auth_bp.route('/users', methods=['GET'])
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, username FROM users')
    users = cursor.fetchall()
    conn.close()

    user_list = [{'id': row['id'], 'username': row['username']} for row in users]
    return jsonify(success=True, users=user_list)

# Endpoint prueba para perfiles
@auth_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT id, username FROM users WHERE id = ?',
        (user_id,)
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify(success=True, user={'id': user['id'], 'username': user['username']})
    else:
        return jsonify(success=False, message='Usuario no encontrado'), 404
