# Crie um programa que leia dois valores e mostre um menu
# na tela inicial com algumas opções

import random
numero_1=int(input('Digite o primeiro valor: '))
numero_2=int(input('Digite o segundo valor: '))
escolha=0
while escolha<5:
    print('''Você digitou os números \033[0;31m{}\033[0m e \033[0;31m{}\033[0m, agora decida o que fazer com eles:
    [1] SOMA
    [2] MULTIPLICAÇÃO
    [3] QUAL É O MAIOR?
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA'''.format(numero_1, numero_2))
    escolha=int(input('Qual é sua opção? '))
    if  escolha==1:
        print('A SOMA dos números escolhidos é \033[0;33m{} + {} = {}\033[0m'.format(numero_1,numero_2,numero_1+numero_2))
    elif escolha==2:
        print('A MULTIPLICAÇÃO dos números escolhidos é \033[0;35m{} x {}\033[0m = {}'.format(numero_1,numero_2,numero_1*numero_2))
    elif escolha==3:
        if numero_1>numero_2:
            print('O número \033[0;31m{} é MAIOR que o número {}\033[0m'.format(numero_1,numero_2))
        elif numero_2>numero_1:
            print('O número \033[0;30m{} é MAIOR que o número {}\033[0m'.format(numero_2,numero_1))
        elif numero_2==numero_1:
            print('Os números \033[0;37m{} e {} são IGUAIS\033[0m'.format(numero_1,numero_2))
    elif escolha==4:
        numero_1=random.randint(0,1000)
        numero_2=random.randint(0,1000)
        print('Os novos números são \033[0;37m{} e {}\033[0m'.format(numero_1,numero_2))
    elif escolha==5:
        print('Finalizando...')
        print('=-=-=-=-=-=-=-=')
        print('Fim.')
    elif escolha>5:
        print('\033[1;31mEscolha inválida\033[0m.')
        escolha=int(input('Qual é sua opção? '))
        if escolha==5:
            print('Finalizando...')
            print('=-=-=-=-=-=-=-=')
            print('Fim.')