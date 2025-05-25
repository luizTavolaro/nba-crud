from models.time import Time
from repository.time_repository import TimeRepository

class TimeController:
    def __init__(self):
        self.repo = TimeRepository()

    def criar_time(self, id, nome, cidade, dataFundacao, tecnico):
        print(f"[CONTROLLER] Criando time {nome}")
        time = Time(id, nome, cidade, dataFundacao, tecnico)
        self.repo.criar(time)

    def listar_times(self):
        print("[CONTROLLER] Listando times")
        return self.repo.listar()

    def atualizar_time(self, id, nome, cidade, dataFundacao, tecnico):
        print(f"[CONTROLLER] Atualizando time id={id}")
        time = Time(id, nome, cidade, dataFundacao, tecnico)
        self.repo.atualizar(time)

    def deletar_time(self, id):
        print(f"[CONTROLLER] Deletando time id={id}")
        self.repo.deletar(id)
