s = cont = 0
while True:
    n = int(input('Insira um numero '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Voce inseriu {cont} numeros e o resultado deles foi {s}')