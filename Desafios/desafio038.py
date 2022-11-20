n1 = int(input('Insira o primeiro número'))
n2 = int(input('Insira o segundo número'))

if n1 > n2:
    print(f'{n1} é o valor maior entre {n1} e {n2}')
elif n2 > n1:
    print(f'{n2} é o valor maior entre {n1} e {n2}')
else:
    print('Não existe valor maior, os dois são iguais')