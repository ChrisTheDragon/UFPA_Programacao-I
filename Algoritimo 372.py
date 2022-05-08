# -------------------------------------------------
# --------------  Algoritmo 372  ------------------
# -------------------------------------------------
from random import shuffle

time = []
rodada = []

for i in range(0, 12):
    time.append(input(f'Digite o nome do {i + 1}º time: '))

shuffle(time)

while True:
    print(f'Entre com o tipo de rodada:\n'
          f'[ 1 ] - Rodada Simples\n'
          f'[ 2 ] - Mata Mata\n'
          f'[ 0 ] - Sair')
    op = int(input('-> '))
    if op == 1:
        for i in range(0, 12):
            for j in range(0, 12):
                if time[i] != time[j]:
                    print(f'[ {time[i]:^15} ] X [ {time[j]:^15} ]')
    elif op == 2:
        for i in range(0, 12):
            if i <= 6:
                print(f'[ {time[i]:^15} ] X [ {time[i + 5]:^15} ]')
    elif op == 0:
        break
    else:
        print('Opção Inválida')
        op = int(input('-> '))
