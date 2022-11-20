valores = []

while True:
    v = int(input('Insira um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não adicionado')
        
    resp = ' ' 
    while resp not in 'SN':
        resp = str(input('Deseja continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break   
        
print(f'Você digitou os valores: {sorted(valores)}')
        