from database import get_database_connection

class Departamento:

    def __init__(self, nombre: str, ubicacion: str, id: int = None) -> None:
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.id = id

class DepartamentoDao:

    @staticmethod
    def fromDbToObject(value: tuple):
        return Departamento(value[1], value[2], value[0])


    @staticmethod
    def read_all() -> list[Departamento]:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM departamentos")
        result = cur.fetchall()
        conn.close()

        return [ DepartamentoDao.fromDbToObject(value) for value in result ]

    @staticmethod
    def read_one(id: int) -> Departamento | None:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM departamentos WHERE id = {id}")
        result = cur.fetchone()
        conn.close()

        return DepartamentoDao.fromDbToObject(result)

    @staticmethod
    def read_one_by_name(name: str) -> Departamento | None:
        conn = get_database_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM departamentos WHERE nombre = '{name}'")
        result = cur.fetchone()
        conn.close()

        return DepartamentoDao.fromDbToObject(result)
