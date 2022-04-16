#-------------------------------------------------
#--------------  Algoritmo 189  ------------------
#-------------------------------------------------
inf = int(input('Menor Temperatura[Fº]: '))
sup = int(input('Maior Temperatura[Fº]: '))
dec = int(input('Decremento: '))

print('\nFarenheit  |  Celsius')
for i in range(inf, sup+1, dec):
  print(f'  [{i}]     |  [{5*(i-32)/9:.2f}]')