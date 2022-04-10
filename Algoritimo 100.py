# -------------------------------------------------
# --------------  Algoritmo 100  -------------------
# -------------------------------------------------
num = int(input(f'Digite um numero: '))
if (num//100) % 4 == 0:
    print(f'{num} é multiplo de 4')
else:
    print(f'{num} não é multiplo de 4')
