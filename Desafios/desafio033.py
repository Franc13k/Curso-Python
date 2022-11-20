from re import A


a = int(input('Insira o primeiro numero'))
b = int(input('Insira o primeiro numero'))
c = int(input('Insira o primeiro numero'))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
    
print(f'O maior valor foi {maior}')
print(f'O menor valor digitado foi {menor}')


