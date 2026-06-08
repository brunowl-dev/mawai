from classes.midias import Filmes, Series, Jogos, Albuns, Midia
from classes.dates import Dates
from classes.tarefas import Tarefas
import os

midias = list()
dates = list()
tarefas = list()

def identificaDono():
    dono = int(input('Quem é o dono da mídia?\n1 - Luiza\n2 - Bruno\n'))
    if (dono == 1):
        return 'Luiza'
    elif (dono == 2):
        return 'Bruno'
    else:
        print('Opção inválida!')
        return False

def addFilmes():
    try:
        nome = input('Digite o nome do filme: ')
        genero = input('Digite o gênero do filme: ')
        duracao = int(input('Digite a duração do filme em minutos: '))
        dono = identificaDono()
        if not dono:
            return False
        midias.append(Filmes(nome, 'Filme', genero, duracao, dono))   
        return True
    except:
        return False
    
def addSeries():
    try:
        nome = input('Digite o nome da série: ')
        genero = input('Digite o gênero da série: ')
        episodios = int(input('Digite a quantidade de episódios da série: '))
        dono = identificaDono()
        if not dono:
            return False
        midias.append(Series(nome, 'Série', genero, episodios, dono))
        return True
    except:
        return False
    
def addJogos():
    try:
        nome = input('Digite o nome do jogo: ')
        genero = input('Digite o gênero do jogo: ')
        plataforma = input('Digite a plataforma do jogo: ')
        dono = identificaDono()
        if not dono:
            return False
        midias.append(Jogos(nome, 'Jogo', genero, plataforma, dono))
        return True
    except:
        return False
    
def addAlbuns():
    try:
        nome = input('Digite o nome do álbum de música: ')
        artista = input('Digite o nome do artista do álbum de música: ')
        genero = input('Digite o gênero do álbum de música: ')
        dono = identificaDono()
        if not dono:
            return False
        midias.append(Albuns(nome, 'Álbum de música', genero, artista, dono))
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

def mostraMidias(*args):
    if (len(midias) == 0):
        print('Nenhuma mídia cadastrada!')
    elif (len(args) > 0):
        if (args[0] == 'Bruno'):
            os.system('cls')
            for midia in midias:
                if (midia.getDono() == 'Bruno'):
                    print(midia)
        elif (args[0] == 'Luiza'):
            os.system('cls')
            for midia in midias:
                if (midia.getDono() == 'Luiza'):
                    print(midia)
        else:
            print('Opção inválida!')
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
        dono = identificaDono()
        if not dono:
            return False
        dates.append(Dates(nome, cidade, estado, data, dono))
        return True
    except:
        return False

def mostraDates(*args):
    if (len(dates) == 0):
        print('Nenhum date cadastrado!')
    elif (len(args) > 0):
        if (args[0] == 'Bruno'):
            os.system('cls')
            for date in dates:
                if (date.getDono() == 'Bruno'):
                    print(date)
        elif (args[0] == 'Luiza'):
            os.system('cls')
            for date in dates:
                if (date.getDono() == 'Luiza'):
                    print(date)
        else:
            print('Opção inválida!')
    else:
        os.system('cls')
        for date in dates:
            print(date)

def addTarefa():
    try:
        nome = input('Digite o nome da tarefa: ')
        descricao = input('Digite a descrição da tarefa: ')
        data = input('Digite a data de vencimento da tarefa (dd/mm/aaaa): ')
        dono = identificaDono()
        if not dono:
            return False
        print('Tarefa cadastrada com sucesso!')
        tarefa = Tarefas(nome, descricao, data, dono)
        tarefas.append(tarefa)
        return True
    except:
        print('Erro ao cadastrar tarefa!')
        return False

def pesquisaTarefas(tarefas):
    try:
        nome = input('Digite o nome da tarefa que deseja pesquisar: ')
        for i, tarefa in enumerate(tarefas):
            if (tarefa.getNome() == nome):
                return i
            
        print('Tarefa não encontrada!')
        return False
    except:
        print('Erro ao pesquisar tarefa!')
        return False

def mostraTarefas(tarefas):
    for tarefa in tarefas:
        print(tarefa)

while True:
    os.system('cls')
    try:
        opcao = int(input('MAWAI\n1 - Cadastrar mídia\n2 - Mostrar mídias\n3 - Cadastrar date\n4 - Mostrar dates\n5 - Cadastrar tarefa\n6 - Mudar status da tarefas\n7 - Mostrar tarefas\n99 - Sair\n'))
    except ValueError:
        print('Valor inválido!')
        os.system('pause')
        continue

    if (opcao == 99):
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

    elif (opcao == 5):
        os.system('cls')
        addTarefa()

    elif (opcao == 6):
        indice = pesquisaTarefas(tarefas)
        if indice is not False:
            print(tarefas[indice])

    elif (opcao == 7):
        mostraTarefas(tarefas)

    else:
        print('Opção inválida!')

    os.system('pause')

print('Programa encerrado!')
os.system('pause')