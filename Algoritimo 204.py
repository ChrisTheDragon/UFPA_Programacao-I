#-------------------------------------------------
#--------------  Algoritmo 204  ------------------
#-------------------------------------------------
num = int(input('Digite o limite de entradas: '))
n = maior = 0
for i in range(0,num):
  n = int(input(f'Digite o {i+1} numero: '))
  if maior < n:
    maior = n
print(f'O maior numero digitado foi {maior}')