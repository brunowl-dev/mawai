#1) registrar filmes, series, jogos ou álbuns de musica - bruno
class Midia:
    def __init__(self, nome, tipo, genero):
        self.nome = nome
        self.tipo = tipo
        self.genero = genero

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo
    
    def setGenero(self, genero):
        self.genero = genero
    
    def getGenero(self):
        return self.genero

    def setLuizasFavorite(self, LuizasFavorite):
        self.LuizasFavorite = LuizasFavorite

    def getLuizasFavorite(self):
        return self.LuizasFavorite

    def setBrunosFavorite(self, BrunosFavorite):
        self.BrunosFavorite = BrunosFavorite

    def getBrunosFavorite(self):
        return self.BrunosFavorite

class Albuns(Midia):
    def __init__(self, nome, tipo, genero, artista):
        super().__init__(nome, tipo, genero)
        self.artista = artista
    
    def setArtista(self, artista):
        self.artista = artista
    
    def getArtista(self):
        return self.artista
    
    def __str__(self):
        return f'Nome: {self.nome} - Tipo: {self.tipo} - Gênero: {self.genero} - Artista: {self.artista}'

class Jogos(Midia):
    def __init__(self, nome, tipo, genero, plataforma):
        super().__init__(nome, tipo, genero)
        self.plataforma = plataforma
    
    def getPlataforma(self):
        return self.plataforma
    
    def setPlataforma(self, plataforma):
        self.plataforma = plataforma

    def __str__(self):
        return f'Nome: {self.nome} - Tipo: {self.tipo} - Gênero: {self.genero} - Plataforma: {self.plataforma}'

class Series(Midia):
    def __init__(self, nome, tipo, genero, episodios):
        super().__init__(nome, tipo, genero)
        self.episodios = episodios
    
    def setEpisodios(self, episodios):
        self.episodios = episodios
    
    def getEpisodios(self):
        return self.episodios
    
    def __str__(self):
        return f'Nome: {self.nome} - Tipo: {self.tipo} - Gênero: {self.genero} - Episódios: {self.episodios}'

class Filmes(Midia):
    def __init__(self, nome, tipo, genero, duracao):
        super().__init__(nome, tipo, genero)
        self.duracao = duracao #Em minutos
    
    def setDuracao(self, duracao):
        self.duracao = duracao
    
    def getDuracao(self):
        return self.duracao
    
    def __str__(self):
        return f'Nome: {self.nome} - Tipo: {self.tipo} - Gênero: {self.genero} - Duração: {self.duracao} minutos'
