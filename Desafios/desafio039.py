ano = int(input('Insira o seu ano de nascimento: '))
idade = 2022 - ano

print(f'Sua idade é {idade}')


if idade < 18:
     print(f'Você tem {idade} e ainda vai se alistar!')
elif idade >= 18 and idade <= 24:
    print(f'Você tem {idade} e precisa se alistar!')
elif idade > 24:
    print(f'Você já passou do tempo de alistamento!')
