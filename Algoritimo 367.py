# -------------------------------------------------
# --------------  Algoritmo 367  ------------------
# -------------------------------------------------
from random import randint

vet = []
som = 0
med = 0
par = 0

for i in range(0, 100):
    vet.append(randint(0, 100))
for i in vet:
    if i % 2 == 0:
        par += 1
    som += i

print(f'Vetor:\n{vet}')
print(f'O maior elemento é: {max(vet)}')
print(f'O menor elemento é: {min(vet)}')
print(f'O percentual de numeros pares é {par}%')
print(f'A média do vetor é: {som/100:.2f}')
