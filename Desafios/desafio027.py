nome = str(input('Digite seu nome completo'))
print(f'Nome: {nome}')
dividido = nome.split()
print(f'Primeiro nome {dividido[0]}')
print(f'Ultimo nome {dividido[len(dividido)-1]}')