from mysql.connector import connect

def get_database_connection():
    return connect(
        host="localhost",
        user="root",
        password="Contraseña321$",
        database="universidad_ampliada"
    )
