from database import get_database_connection

class Curso:
    def __init__(self, nombre: str, descripcion: str, creditos: int, departamento_id: int = None, id: int = None, nombre_departamento: str = None) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.creditos = creditos
        self.departamento_id = departamento_id
        self.id = id
        self.nombre_departamento = nombre_departamento

class CursoDao: # Data Access Object

    @staticmethod
    def fromDbToObject(value: tuple) -> Curso:
        return Curso(value[1], value[2], value[3], value[4], value[0])

    @staticmethod
    def create(curso: Curso) -> None:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO cursos (nombre, descripcion, creditos, departamento_id) VALUES (%s, %s, %s, %s)",
                    (curso.nombre, curso.descripcion, curso.creditos, curso.departamento_id))
        conn.commit()
        conn.close()

    @staticmethod
    def read_all() -> list[Curso]:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM cursos")
        result = cur.fetchall()
        conn.close()

        return [ CursoDao.fromDbToObject(value) for value in result ]

    @staticmethod
    def read_one(id: int) -> Curso | None:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM cursos WHERE id = {id}")
        result = cur.fetchone()
        conn.close()

        if result == None:
            return None
        
        return CursoDao.fromDbToObject(result)

    @staticmethod
    def update(curso: Curso) -> None:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute("""
                    UPDATE cursos
                    SET nombre = %s,
                        descripcion = %s,
                        creditos = %s,
                        departamento_id = %s
                    WHERE id = %s
                    """,
                    (curso.nombre, curso.descripcion, curso.creditos, curso.departamento_id, curso.id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM cursos WHERE id = {id}")
        conn.commit()
        conn.close()

