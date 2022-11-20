palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'estudar', 'programador')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')