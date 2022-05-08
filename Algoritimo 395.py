# -------------------------------------------------
# --------------  Algoritmo 395  ------------------
# -------------------------------------------------
entradas = []
pessoas = []
flag = 0
cont = 0

while True:
    esp = str(' ')
    print(f'-'*40)
    print(f'{esp:^17}MENU')
    print(f'-'*40)
    print(f'[ 1 ] - INSERIR\n'
          f'[ 2 ] - ORDENAR\n'
          f'[ 3 ] - LISTAR\n'
          f'[ 4 ] - PROCURAR\n'
          f'[ 5 ] - SAIR')
    op = int(input('-> '))

    if op == 1:
          print(f'Entre com os nomes e salários: ')
          while True:
                entradas.append(input('Digite o Nome: '))
                entradas.append(float(input('Digite o salário: R$')))
                while entradas[1] <= 0:
                    print('Não existe salário negativo!')
                    entradas.pop()
                    entradas.append(float(input('Digite o salário: ')))
                pessoas.append(entradas[:])
                entradas.clear()

                flag += 1

                es = str(input(f'Deseja continuar cadastrando?[S/N] ')).upper()[0]
                while es not in 'SsNn':
                    print('Opcão Inválida!')
                    es = str(input(f'Deseja continuar cadastrando?[S/N] ')).upper()[0]
                if es in 'Nn':
                    break
                elif es in 'Ss':
                    continue
    elif op == 2:
        if flag == 0:
            print('Não há Pessoas Cadastradas')
            continue
        else:
            pessoas.sort()
            print(f'----NOME---|--SALÁRIO--')
            for i in range(0, len(pessoas)):
                print(f'{pessoas[i][0]:^10} | R${pessoas[i][1]:^10.2f}')
    elif op == 3:
        if flag == 0:
            print('Não há Pessoas Cadastradas')
            continue
        else:
            print(f'----NOME---|--SALÁRIO--')
            for i in range(0, len(pessoas)):
                print(f'{pessoas[i][0]:^10} | R${pessoas[i][1]:^10.2f}')
    elif op == 4:
        if flag == 0:
            print('Não há Pessoas Cadastradas')
            continue
        else:
            nome = str(input(f'Entre com o nome: '))
            for i in range(0, len(pessoas)):
                if pessoas[i][0] == nome:
                    print('Pessoa Encontrada:')
                    print(f'{pessoas[i][0]:^10} | R${pessoas[i][1]:^10.2f}')
                    cont = 1
                if cont == 0:
                    print('Pessoa não encontrada!')
                    break
    elif op == 5:
        print(f'Programa Finalizado!')
        break
    else:
        print('Opção Inválida!\n')
