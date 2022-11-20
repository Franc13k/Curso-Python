soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Insira um número: '))
    if num % 2 == 0:
        soma += num
        cont += + 1
print(f'Você informou {cont} números pares e a soma foi {soma}')
