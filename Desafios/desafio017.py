from math import hypot

cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
hi = hypot(cato, cata)

print(f'A hipotenusa é {hi}')