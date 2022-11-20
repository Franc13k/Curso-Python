totfator = 0
repeat = 0
while repeat != 1:
    number = int(input('Digite um valor: '))
    repeat += 1
    totfator = number
    print('{}'.format(number),end=''),
    for fat in range(1, number):
        totfator = totfator * fat
        print('x{}'.format(fat),end='')
    print(f' = {totfator:^3}')
print('A Múltiplicação da Fatoração do número {} é {}'.format(number,totfator))