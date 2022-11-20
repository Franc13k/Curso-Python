def voto(ano=0):
    idade = 2022 - ano
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos, voto obrigatório!'
    elif idade < 16:
        return f'Com {idade} anos, não vota!'
    elif (idade >= 16 and idade <= 17) or idade >= 65:
        return f'Com {idade} anos, voto opcional!'
    else:
        return 'ERRO! Insira o ano correto!'
    

y = int(input('Informe o ano de nascimento: '))
print(voto(y))