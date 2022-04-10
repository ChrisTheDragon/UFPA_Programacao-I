# -------------------------------------------------
# --------------  Algoritmo 124  ------------------
# -------------------------------------------------
t = ''
s1 = float(input('Primiro seguimento: '))
s2 = float(input('41mSegundo seguimento: '))
s3 = float(input('44mTerceiro seguimento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 > s2 and s1 > s3:
        maior = s1*2
        lados = (s2*2)+s3*2
    elif s2 > s3:
        maior = s2*2
        lados = (s1*2)+s3*2
    else:
        maior = s3 * 2
        lados = (s1 * 2) + s2 * 2

    if maior == lados:
        t = 'Retangulo'
    elif maior > lados:
        t = 'Obtusangulo'
    else:
        t = 'Acutangulo'

    print(f'{s1}, {s2} e {s3} podem ser lados de um triângulo {t}!')
else:
    print(f'{s1}, {s2} e {s3} NÃO podem ser lados de um triângulo!')
