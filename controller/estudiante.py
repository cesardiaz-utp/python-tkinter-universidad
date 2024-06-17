
from model.estudiante import Estudiante, EstudianteDao


class EstudianteController:

    @staticmethod
    def get_all():
        return EstudianteDao.read_all()

    @staticmethod
    def get_by_id(id: int) -> Estudiante:
        est = EstudianteDao.read(id)
        return est
    
    @staticmethod
    def new(nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion):
        est = Estudiante(nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion)
        EstudianteDao.create(est)

    @staticmethod
    def modify(id, nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion):
        est = Estudiante(nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion, id)
        EstudianteDao.update(est)

    @staticmethod
    def delete(id):
        EstudianteDao.delete(id)
    