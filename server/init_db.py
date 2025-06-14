import sqlite3
import os

# Ruta absoluta a la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.sqlite')

# Usuarios de prueba
users_to_insert = [
    ('admin', 'admin'),
    ('brianparedes', 'brianparedes'),
    ('choco', 'choco'),
    ('juan@mail.com', 'clave123'),
    ('maria@mail.com', '123456'),
    ('test@mail.com', 'testpass'),
    ('rodrigo08@gmail.com', 'putete'),
    ('petete', 'petete')
]

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    for username, password in users_to_insert:
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user:
            # Si existe, actualizo la contraseña
            cursor.execute(
                'UPDATE users SET password = ? WHERE username = ?',
                (password, username)
            )
            print(f'🔄 Usuario {username} actualizado con nueva contraseña')
        else:
            # Si no existe, inserto
            cursor.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)',
                (username, password)
            )
            print(f'✅ Usuario {username} insertado correctamente')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()
