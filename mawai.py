from midias import Filmes, Series, Jogos, Albuns, Midia
import os

midias = list()

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
        genero = input('Digite o gênero do álbum de música: ')
        artista = input('Digite o nome do artista do álbum de música: ')
        midias.append(Albuns(nome, 'Álbum de música', genero, artista))
        return True
    except:
        return False

while True:
    os.system('cls')
    opcao = int(input('MAWAI\n1 - Cadastrar mídia\n2 - Mostrar mídias\n3 - Sair\n'))

    if (opcao == 3):
        break

    elif (opcao == 1):
        os.system('cls')
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

    elif (opcao == 2):
        if (len(midias) == 0):
            print('Nenhuma mídia cadastrada!')
        else:
            for midia in midias:
                print(midia)
    
print('Programa encerrado!')
os.system('pause')