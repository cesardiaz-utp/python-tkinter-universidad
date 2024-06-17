from model.departamento import DepartamentoDao


class DepartamentoController:
    @staticmethod
    def get_all():
        return DepartamentoDao.read_all()
    
    @staticmethod
    def get_by_id(id: int):
        departamento = DepartamentoDao.read_one(id)
        return departamento
    
    @staticmethod
    def get_by_name(name: str):
        departamento = DepartamentoDao.read_one_by_name(name)
        return departamento