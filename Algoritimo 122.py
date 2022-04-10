# -------------------------------------------------
# --------------  Algoritmo 122  ------------------
# -------------------------------------------------
s1 = float(input('Primiro seguimento: '))
s2 = float(input('41mSegundo seguimento: '))
s3 = float(input('44mTerceiro seguimento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print(f'{s1}, {s2} e {s3} podem ser lados de um triângulo!')
else:
    print(f'{s1}, {s2} e {s3} NÃO podem ser lados de um triângulo!')