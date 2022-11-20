valores = []
pos_maior = []
pos_menor = []
for cont in range(0,5):
    valores.append(int(input('Insira um valor: ')))
    
for pos, v in enumerate(valores):
    if v == max(valores):
        pos_maior.append(pos)
    if v == min(valores):
        pos_menor.append(pos)
print(f'O maior valor digitado na lista foi {max(valores)} e está na posição {pos_maior}')
print(f'O menor valor digitado na lista foi {min(valores)} e está na posição {pos_menor}')