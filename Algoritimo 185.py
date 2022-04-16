#-------------------------------------------------
#--------------  Algoritmo 185  ------------------
#-------------------------------------------------
from math import sqrt

num = []

for i in range(0,15):
  num.append(int(input('Digite um numero: ')))

for i in range(0,15):
  if num[i] > 0:
    print(f'[{sqrt(num[i]):.2f}]', end='')
  else:
    print('Não faço raiz de numero negativo')