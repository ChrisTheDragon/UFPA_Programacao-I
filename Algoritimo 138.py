# -------------------------------------------------
# --------------  Algoritmo 138  ------------------
# -------------------------------------------------
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
         'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')
num = int(input('Digite um número: '))

for i in range(len(meses)):
    if num == i+1:
        print(f'Voce Digitou: {meses[i]}')
    else:
        print('Não há mês para esse número!')
        break
