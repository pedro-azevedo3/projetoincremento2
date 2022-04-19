opcao = 0
manifestacao = []
sujestoes = []
reclamacoes = []
elogios = []
criarmanifestacao = []
protocolo = []
addreclamacao = []
addsujestao = []
addelogio = []
nome = []
while True:
    if opcao >= 7:
        pass
    else:
        print('\033[33m''======= OUVIDORIA ABC =======''\033[0;0m')
    print()
    print('\033[33m''1) LISTAR TODAS AS MANIFESTAÇÕES''\033[0;0m')
    print()
    print('\033[33m''2) LISTAR TODAS AS SUJESTÕES''\033[0;0m')
    print()
    print('\033[33m''3) LISTAR TODAS AS RECLAMAÇÕES''\033[0;0m')
    print()
    print('\033[33m''4) LISTAR TODOS OS ELOGIOS''\033[0;0m')
    print()
    print('\033[33m''5) ENVIAR UMA MANIFESTAÇÃO (criar uma nova)''\033[0;0m')
    print()
    print('\033[33m''6) PESQUISAR PELO NÚMERO DO PROTOCOLO (ID)''\033[0;0m')
    print()
    print('\033[33m''7) SAIR''\033[0;0m')
    print()
    opcao = int(input('\033[33m''DIGITE A OPÇÃO DESEJADA: ''\033[0;0m'))

    if opcao == 1:
        nomes = input('DIGITE O SEU NOME: ')
        nome.append([nomes])
        tipo = int(input('DIGITE O TIPO DA MANIFESTAÇÃO: 1) PARA RECLAMAÇÃO, 2) PARA SUJESTÃO E 3)ELOGIO: '))
        if tipo == 1:
            print('\033[1;35m''VOCÊ SELECIONOU RECLAMAÇÃO.''\033[0;0m')
            addreclamacao = str(input('DIGITE A DESCRIÇÃO: '))
            reclamacoes.append([addreclamacao])

        elif tipo == 2:
            print('\033[1;35m''VOCÊ SELECIONOU SUJESTÃO.''\033[0;0m')
            addsujestao = str(input('DIGITE A DESCRIÇÃO: '))
            sujestoes.append([addsujestao])

        else:
            print('\033[1;35m''VOCÊ SELECIONOU ELOGIO.''\033[0;0m')
            addelogio = str(input('DIGITE A DESCRIÇÃO: '))
            elogios.append([addelogio])
    elif opcao == 2:
        print(f'NOME DO REQUISITANTE:{nome}, E A SUJESTÃO FOI: {sujestoes}')

    elif opcao == 3:
        print(f'NOME DO REQUISITANTE: {nome}, E A RECLAMAÇÃO FOI: {reclamacoes}')

    elif opcao == 4:
        print(f'NOME DO REQUISITANTE: {nome}, E O ELOGIO FOI: {elogios}')

    elif opcao == 5:
        print()
        nomes = input('\033[1;95m''DIGITE O SEU NOME: ''\033[0;0m')
        nome.append([nomes])
        tipo = int(input('\033[1;95m''DIGITE O TIPO DA MANIFESTAÇÃO: 1) PARA RECLAMAÇÃO, 2) PARA SUJESTÃO E 3)ELOGIO: '
                         '\033[0;0m'))
        if tipo == 1:
            print('\033[1;35m''VOCÊ SELECIONOU RECLAMAÇÃO.''\033[0;0m')
            addreclamacao = str(input('DIGITE A DESCRIÇÃO: '))
            reclamacoes.append([addreclamacao])

        elif tipo == 2:
            print('\033[1;35m''VOCÊ SELECIONOU SUJESTÃO.''\033[0;0m')
            addsujestao = str(input('DIGITE A DESCRIÇÃO: '))
            sujestoes.append([addsujestao])

        else:
            print('\033[1;35m''VOCÊ SELECIONOU ELOGIO.''\033[0;0m')
            addelogio = str(input('DIGITE A DESCRIÇÃO: '))
            elogios.append([addelogio])
    elif opcao == 6:
        print()
        protocolo = int(input('DIGITE O NUMERO DO PROTOCOLO DESEJADO: '))
    else:
        break
