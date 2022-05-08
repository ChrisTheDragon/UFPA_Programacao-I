# -------------------------------------------------
# --------------  Algoritmo 371  ------------------
# -------------------------------------------------
from random import randint

vet1 = []
vet2 = []
vet3 = []

for i in range(0, 10):
    vet1.append(randint(0, 100))
for i in range(0, 20):
    vet2.append(randint(0, 100))

for i in vet2:
    for j in vet1:
        if j == i:
            if j not in vet3:
                vet3.append(j)

print(f'Conjunto 1: {vet1}')
print(f'Conjunto 2: {vet2}')
print(f'Os elemntos comuns nos dois conjuntos são: {vet3}')