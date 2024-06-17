from database import get_database_connection

class Estudiante:

    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: str, genero: str, email: str, telefono: str, direccion: str, id: int = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

class EstudianteDao: # DAO -> Data Access Object  -> Clase utilitaria para acceder a los datos de una tabla

    @staticmethod
    def create(est: Estudiante):
        conn = get_database_connection()

        q = conn.cursor()
        q.execute(f"INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion) VALUES ('{est.nombre}', '{est.apellido}', '{est.fecha_nacimiento}', '{est.genero}', '{est.email}', '{est.telefono}', '{est.direccion}')")
        
        conn.commit()

        conn.close()
    
    @staticmethod
    def read(id: int) -> Estudiante | None:
        conn = get_database_connection()

        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM estudiantes WHERE id = {id}")
        # tuple -> (1, 'Cesar', 'Diaz',...)

        result = cursor.fetchone()

        conn.close()

        if result == None:
            return None

        return Estudiante(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[0])
    
    @staticmethod
    def read_all() -> list[Estudiante]:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM estudiantes")

        result = cur.fetchall()

        conn.close()

        # response = []
        # for est in result:
        #     response.append(Estudiante(est.nombre, est.apellido, est.fecha_nacimiento, est.genero, est.email, est.telefono, est.direccion, est.id))


        response = [ Estudiante(est[1], est[2], est[3], est[4], est[5], est[6], est[7], est[0]) for est in result ]

        return response
    
    @staticmethod
    def update(estudiante: Estudiante) -> None:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute(f"""
                    UPDATE estudiantes
                    SET nombre = '{estudiante.nombre}',
                        apellido = '{estudiante.apellido}',
                        fecha_nacimiento = '{estudiante.fecha_nacimiento}',
                        genero = '{estudiante.genero}',
                        email = '{estudiante.email}',
                        telefono = '{estudiante.telefono}',
                        direccion = '{estudiante.direccion}'
                    WHERE id = {estudiante.id}
                    """)

        conn.commit()

        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM estudiantes WHERE id = {id}")

        conn.commit()
        conn.close()


