from midias import Filmes, Series, Jogos, Albuns, Midia
from dates import Dates
import os

midias = list()
dates = list()

def addFilmes():
    try:
        nome = input('Digite o nome do filme: ')
        genero = input('Digite o gênero do filme: ')
        duracao = int(input('Digite a duração do filme em minutos: '))
        midias.append(Filmes(nome, 'Filme', genero, duracao))   
        return True
    except:
        return False
    
def addSeries():
    try:
        nome = input('Digite o nome da série: ')
        genero = input('Digite o gênero da série: ')
        episodios = int(input('Digite a quantidade de episódios da série: '))
        midias.append(Series(nome, 'Série', genero, episodios))
        return True
    except:
        return False
    
def addJogos():
    try:
        nome = input('Digite o nome do jogo: ')
        genero = input('Digite o gênero do jogo: ')
        plataforma = input('Digite a plataforma do jogo: ')
        midias.append(Jogos(nome, 'Jogo', genero, plataforma))
        return True
    except:
        return False
    
def addAlbuns():
    try:
        nome = input('Digite o nome do álbum de música: ')
        artista = input('Digite o nome do artista do álbum de música: ')
        genero = input('Digite o gênero do álbum de música: ')
        midias.append(Albuns(nome, 'Álbum de música', genero, artista))
        return True
    except:
        return False

def addMidia():
    tipo_midia = int(input('1-Filme\n2-Série\n3-Jogo\n4-Álbum de música\n'))
    if (tipo_midia == 1):
        if (addFilmes()):
            print('Mídia cadastrada com sucesso!')
        else:
            print('Erro ao cadastrar mídia!')
    elif (tipo_midia == 2):
        if (addSeries()):
            print('Mídia cadastrada com sucesso!')
        else:
            print('Erro ao cadastrar mídia!')
    elif (tipo_midia == 3):
        if (addJogos()):
            print('Mídia cadastrada com sucesso!')
        else:
            print('Erro ao cadastrar mídia!')
    elif (tipo_midia == 4):
        if (addAlbuns()):
            print('Mídia cadastrada com sucesso!')
        else:
            print('Erro ao cadastrar mídia!')
    else:
        print('Opção inválida!')

def mostraMidias():
    if (len(midias) == 0):
        print('Nenhuma mídia cadastrada!')
    else:
        os.system('cls')
        for midia in midias:
            print(midia)

def addDate():
    try:
        nome = input('Digite o nome do evento: ')
        cidade = input('Digite a cidade do evento: ')
        estado = input('Digite o estado do evento: ')
        data = input('Digite a data do evento (dd/mm/aaaa): ')
        dates.append(Dates(nome, cidade, estado, data))
        return True
    except:
        return False

def mostraDates():
    if (len(dates) == 0):
        print('Nenhum date cadastrado!')
    else:
        os.system('cls')
        for date in dates:
            print(date)

while True:
    os.system('cls')
    opcao = int(input('MAWAI\n1 - Cadastrar mídia\n2 - Mostrar mídias\n3 - Cadastrar date\n4 - Mostrar dates\n5 - Sair\n'))

    if (opcao == 5):
        break

    elif (opcao == 1):
        os.system('cls')
        addMidia()

    elif (opcao == 2):
        mostraMidias()
    
    elif (opcao == 3):
        os.system('cls')
        addDate()
    
    elif (opcao == 4):
        mostraDates()

    os.system('pause')
    
print('Programa encerrado!')
os.system('pause')