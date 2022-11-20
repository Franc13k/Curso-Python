tentativas = 0
soma = 0
num = int(input('digite 999: '))
while num != 999:
 tentativas += 1
 soma += num
 num = int(input('por favor digite 999: '))
if tentativas == 0:
 print('você é muito bonzinho, digitou 999 de prima!')
else:
 print('você é muito levado, digitou {} numeros antes de digitar 999'.format(tentativas))
 print('a soma dos numeros digitados foi de {}'.format(soma))