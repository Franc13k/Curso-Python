num = int(input('Insira um numero para verificar se é impar ou par'))
res = num % 2

if res == 0:
    print('Este numero é par')
else:
    print('Este numero é impar')