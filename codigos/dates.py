class Dates:
    def __init__(self, nome, cidade, estado, data):
        self.nome = nome
        self.cidade = cidade
        self.estado = estado
        self.data = data
    
    def __str__(self):
        return f"{self.nome} - {self.cidade} - {self.estado} - {self.data}"

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getCidade(self):
        return self.cidade
    
    def setCidade(self, cidade):
        self.cidade = cidade
    
    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data