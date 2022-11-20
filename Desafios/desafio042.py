a = int(input('Insira o valor do primeiro lado: '))
b = int(input('Insira o valor do segundo lado: '))
c = int(input('Insira o valor do terceiro lado: '))

if a == b and a == c and b == c:
    print('Este é um triângulo equilátero')
elif a == b and a != c or b == c and a != b or a == c and b != c:
    print('Este é um triângulo isósceles')
elif a != b and a != c and b != c:
    print('Este é um triângulo escaleno')

