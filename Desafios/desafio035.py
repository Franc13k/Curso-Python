r1 = float('Insira o primeiro segmento: ')
r2 = float('Insira o segundo segmento: ')
r3 = float('Insira o terceiro segmento: ')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')