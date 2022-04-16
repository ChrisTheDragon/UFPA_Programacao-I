#-------------------------------------------------
#--------------  Algoritmo 210  ------------------
#-------------------------------------------------
result = []
result.append(int(input('Digite o primiero termo: ')))
result.append(int(input('Digite o segundo termo: ')))
for i in range(2, 11):
  if i%2 == 0:
    result.append(result[i-1] + result[i-2])
  else:
    result.append(result[i-1] - result[i-2])
  
for i in range(0,10):
  print(f'[{result[i]}]', end='')