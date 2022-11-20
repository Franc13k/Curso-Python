ano = int(input('Insira o ano de seu nascimento: '))
for c in range(0, 7):
    print(ano)
    idade = 2022 - ano
    if idade < 18:
        print(f'{c} pessoas não atingiram a maior idade:')
    else:
        print('Atingiu a maior idade!')