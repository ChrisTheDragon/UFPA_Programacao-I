#-------------------------------------------------
#--------------  Algoritmo 25  -------------------
#-------------------------------------------------
data = int(input(f'Digite uma data no formato DDMMAA: '))
dia = data // 10000
mes = data % 10000 // 100
ano = data % 100

print(f'Dia: {dia}')
print(f'Mês: {mes}')
print(f'Ano: {ano}')