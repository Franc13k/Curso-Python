ano = int(input('Insira o ano'))
dias = int(input('Insira quantos dias ele teve'))
print(f'Seu ano é {ano}')
if dias <= 365:
    print('Este não é um ano bissexto')
else:
    print('Este é um ano bissexto')