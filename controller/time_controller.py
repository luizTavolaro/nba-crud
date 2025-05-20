from models.time import Time
from repository.time_repository import TimeRepository

class TimeController:
    def __init__(self):
        self.repo = TimeRepository()

    def criar_time(self, id, nome, cidade, dataFundacao, tecnico):
        time = Time(id, nome, cidade, dataFundacao, tecnico)
        self.repo.criar(time)

    def listar_times(self):
        return self.repo.listar()

    def atualizar_time(self, id, nome, cidade, dataFundacao, tecnico):
        time = Time(id, nome, cidade, dataFundacao, tecnico)
        self.repo.atualizar(time)

    def deletar_time(self, id):
        self.repo.deletar(id)

