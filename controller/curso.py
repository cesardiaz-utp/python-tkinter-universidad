from model.curso import Curso, CursoDao
from model.departamento import DepartamentoDao


class CursoController:

    @staticmethod
    def new(nombre: str, descripcion: str, creditos: int, departamento_id: int):
        curso = Curso(nombre, descripcion, creditos, departamento_id)
        CursoDao.create(curso)

    @staticmethod
    def modify(id: int, nombre: str, descripcion: str, creditos: int, departamento_id: int):
        curso = CursoDao.read_one(id)
        curso.nombre = nombre
        curso.descripcion = descripcion
        curso.creditos = creditos
        curso.departamento_id = departamento_id

        CursoDao.update(curso)

    @staticmethod
    def delete(id: int):
        CursoDao.delete(id)

    @staticmethod
    def get_all():
        cursos = CursoDao.read_all()
        for curso in cursos:
            departamento = DepartamentoDao.read_one(curso.departamento_id)
            curso.nombre_departamento = departamento.nombre

        return cursos
    
    @staticmethod
    def get_by_id(id: int):
        curso = CursoDao.read_one(id)
        
        if curso == None:
            return None
        
        departamento = DepartamentoDao.read_one(curso.departamento_id)
        curso.nombre_departamento = departamento.nombre
        return curso
