import random
from time import sleep
t = 1

print('--- Desafio de adivinhar! ---')
n1 = random.randint(1,10)
print('Vou pensar em um número de 1 a 10 e você tem que adivinhar')
sleep(0.5)
print('Pensando...')
sleep(0.8)
n2 = int(input('Pensei! Agora tente adivinhar: '))
while n2 != n1:
    n2 = int(input('Errou! Tente de novo: '))
    t += 1
print(f'Parabens vc acertou na {t} tentativa, o meu numero escolhido foi {n1}')