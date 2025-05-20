class Time:
    def __init__(self, id, nome, cidade, dataFundacao, tecnico):
        self.id = id
        self.nome = nome
        self.cidade = cidade
        self.dataFundacao = dataFundacao
        self.tecnico = tecnico
        
    def to_dict(self):
        return self.__dict__