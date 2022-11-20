x = int(input('Insira o primeiro valor: '))
y = int(input('Insira o segundo valor: '))
z = int(input('Insira o terceiro valor: '))
c = int(input('Insira o quarto valor: '))
cont = 0
val = (x, y, z, c)

print(f'Os valores digitados foram: {val}')
print(f'O número 9 apareceu {val.count(9)} vezes')
print(f'O primeiro número 3 digitado foi na {val.index(3)} posição')

if (x%2) == 0:
    print(f'O número {x} é par')
    cont += 1
if (y%2) == 0:
    print(f'O número {y} é par')
    cont += 1
if (z%2) == 0:
    print(f'O número {z} é par')
    cont += 1
if (c%2) == 0:
    print(f'O número {c} é par')
    cont += 1

print(f'Foram digitados {cont} pares')
