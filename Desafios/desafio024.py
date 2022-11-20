nome = str(input('Insira o nome da sua cidade:'))
busca = 'Santo' in nome

if busca==True:
    print(f'{busca} Sua cidade tem "Santo" no nome')
else:
    print(f'{busca} Sua cidade não tem "Santo" no nome')