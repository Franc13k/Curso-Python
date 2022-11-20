dados = [[], []]
valor = 0

for cont in range(1,8):
    valor = int(input('Insira o valor: '))
    
    if (valor % 2) == 0:
        dados[0].append(valor)
    else:
        dados[1].append(valor)
print(f'Todos os valores foram {dados}')
print(f'Os valores pares foram {sorted(dados[0])}')
print(f'Os valores impares foram {sorted(dados[1])}')