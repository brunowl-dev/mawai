class Tarefas:
    def __init__(self, nome, descricao, data):
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.status = 'Pendente'

    def __str__(self):
        return f'{self.nome} - {self.descricao} - {self.data}'
    
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setDescricao(self, descricao):
        self.descricao = descricao
    
    def getDescricao(self):
        return self.descricao
    
    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
    
    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status