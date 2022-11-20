#Faça um algoritmo que leia o salário de um funcionário e mostre seu
#novo salário com 15% de aumento.

preco = float(input('Insira o salário do funcionário: '))
d = preco * 0.15 
s = preco + d
print(f'O valor do salário com 15"%" de aumento é R${s}')