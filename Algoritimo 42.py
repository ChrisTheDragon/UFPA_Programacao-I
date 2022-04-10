#-------------------------------------------------
#--------------  Algoritmo 42  -------------------
#-------------------------------------------------
import math
ang = float(input('Digite o angulo em graus: '))
print(f'Seno: {math.sin(math.radians(ang)):.2f}')
print(f'Coseno: {math.cos(math.radians(ang)):.2f}')
print(f'Tangente: {math.tan(math.radians(ang)):.2f}')
print(f'Secante: {1/(math.sin(math.radians(ang))):.2f}')
print(f'Co-Secante: {1/(math.acos(math.radians(ang))):.2f}')
print(f'Co-Tangente: {1/(math.atan(math.radians(ang))):.2f}')