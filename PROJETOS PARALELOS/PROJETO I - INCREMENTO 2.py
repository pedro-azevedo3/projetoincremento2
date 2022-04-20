from encodings import search_function
from msilib.schema import Class

option = 5
listOfAllManifestations = []


class manifestation(object):
    def __init__(self, typeInput, NameInput, protocolInput, content):
        self.type = typeInput
        self.name = NameInput
        self.protocol = protocolInput
        self.content = content


while True:
    if 0 < option > 4:
        print(
            '\n =====OUVIDORIA ABC=====\n \n 1) LISTAR TODAS AS MANIFESTAÇÕES \n '
            '2) ENVIAR UMA MANIFESTAÇÃO (criar uma nova)'
            '\n 3) PESQUISAR PELO NÚMERO DE PROTOCOLO (ID)\n 4) SAIR\n')

    if option == 1:

        searchInput = int(input(
            '\nDIGITE O TIPO DA MANIFESTAÇÃO QUE VOCÊ DESEJA VER:\n 1)RECLAMAÇÕES \n 2)SUJESTÕES '
            '\n 3)ELOGIOS \n \nQUAL SUA ESCOLHA?: '))

        search = ''

        if searchInput == 1:
            search = 'claim'
        elif searchInput == 2:
            search = 'suggestion'
        elif searchInput == 3:
            search = 'compliment'

        for element in listOfAllManifestations:
            if element.type == search:
                print(f'\nNome: {element.name}\nProtocolo: {element.protocol}\nConteúdo: {element.content}\n')

        keep = False
        while not keep:
            keepInput = int(input('Continuar? Sim (1) / Não (0)\n '))
            if keepInput == 1:
                option = 5
                keep = True
            elif keepInput == 0:
                option = 4
                keep = True

    if option == 2:
        nameInput = input('QUAL SEU NOME?: ')
        typeNum = int(input(
            '\n DIGITE O TIPO DA MANIFESTAÇÃO QUE VOCÊ DESEJA ENVIAR:\n 1)RECLAMAÇÕES \n 2)SUJESTÕES \n 3)ELOGIOS \n'
            ' \nQUAL SUA ESCOLHA?: '))
        contentInput = input('\nQUAL A MANIFESTAÇÃO QUE VOCÊ DESEJA FAZER? ')
        protocolInput = input('\nESCOLHA UM NÚMERO PARA O PROTOCOLO DA SUA MANIFESTAÇÃO: ')

        typeInput = ''

        if typeNum == 1:
            typeInput = 'claim'
        elif typeNum == 2:
            typeInput = 'suggestion'
        elif typeNum == 3:
            typeInput = 'compliment'

        listOfAllManifestations.append(manifestation(typeInput, nameInput, protocolInput, contentInput))

        option = 5

    elif option == 4:
        break

    else:
        aa = int(input('DIGITE A OPÇÃO DESEJADA: '))
        option = aa
        pass