# -------------------------------------------------
# --------------  Algoritmo 123  ------------------
# -------------------------------------------------
t = ''
s1 = float(input('Primiro seguimento: '))
s2 = float(input('41mSegundo seguimento: '))
s3 = float(input('44mTerceiro seguimento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        t = 'Equilátero'
    elif s1 == s2 or s2 == s3 or s3 == s1:
        t = 'Isósceles'
    elif s1 != s2 and s2 != s3 and s3 != s1:
        t = 'Escaleno'
    print(f'{s1}, {s2} e {s3} podem ser lados de um triângulo {t}!')
else:
    print(f'{s1}, {s2} e {s3} NÃO podem ser lados de um triângulo!')
