#-------------------------------------------------
#--------------  Algoritmo 44  -------------------
#-------------------------------------------------
from math import log
num = float(input('Digite um número: '))
base = float(input('Digite uma base: '))
print(f'O logaritimo de {num} na base {base} é {log(num)/log(base):.2f}')