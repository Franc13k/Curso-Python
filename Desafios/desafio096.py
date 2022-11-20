def area(l, c):
    s = l * c
    print(f'As dimensões do terreno {l} x {c} é {s}m2')

l = float(input('Insira a largura do terreno: '))
c = float(input('Insira o comprimento do seu terreno: '))
area(l, c)