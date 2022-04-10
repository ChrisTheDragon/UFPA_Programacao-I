# -------------------------------------------------
# --------------  Algoritmo 97  -------------------
# -------------------------------------------------
n = int(input('Digite um numero: '))

if n % 10 == 0:
    print(f'{n} é divisivel por 10')
elif n % 5 == 0:
    print(f'{n} é divisivel por 5')
elif n % 2 == 0:
    print(f'{n} é divisivel por 2')
else:
    print(f'{n} não é divisivel por 10, 5 ou 2')