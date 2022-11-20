valores = []
for cont in range(0,5):
    v = int(input('Insira o valor: '))
    if cont == 0 or v > valores[-1]:
        valores.append(v)
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
                valores.insert(pos, v)
                break
            pos += 1
print(f'Os valores inseridos foram {valores}')