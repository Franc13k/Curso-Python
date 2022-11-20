import random
num = random.randint(1, 5)
print('Número sorteado, boa sorte!')
desc = int(input('Tente descobrir qual o numero de 1 a 5:'))
if desc == num:
    print(f'Número sorteado foi {num}')
    print('Parabéns, você acertou o número!')
else:
    print(f'Número sorteado foi {num}')
    print('Você errou, tente novamente!')
