# -------------------------------------------------
# --------------  Algoritmo 119  ------------------
# -------------------------------------------------
lista = []
for i in range(0,3):
    lista.append(int(input('Digite um Número: ')))
lista.sort(reverse=True)
print(f'Ordem decrescente = {lista}')