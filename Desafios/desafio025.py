nome = str(input('Insira seu nome completo:'))
busca = 'Silva' in nome

if busca==True:
    print(f'{busca} Seu nome tem "Silva" nele')
else:
    print(f'{busca} Seu nome não tem "Silva" nele')
