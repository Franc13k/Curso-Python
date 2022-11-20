valores = []
pos = 0
while True:
    valores.append(int(input('Insira um número: ')))
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
    
print(f'Foram digitado {len(valores)} numeros')
print(f'A lista ordenada de forma decrescente é: {sorted(valores, reverse=True)}')
if 5 in valores:
    pos = valores.index(5)
    print(f'O valor 5 foi adicionado e está na posição {pos}')
else:
    print(f'O valor 5 não foi adicionado')
        