frase = str(input('Digite o seu nome completo:'))
maius = frase.upper()
minus = frase.lower()
qnt = len(frase.strip())
dividido = frase.split()

print('Maiusculo: {}' .format(maius))
print('Minusculo: {}' .format(minus))
print('Quantidade de letras: {}' .format(qnt))
print('Quantidade letras primeiro nome: ', len(dividido[0]))