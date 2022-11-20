dados = list()
pessoas = list()
totpes = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
    
    for p in pessoas:
        totpes += 1
        
print(f'Foram cadastradas {totpes} pessoas')
print(f'O maior peso foi de {max(pessoas)}')
for p in pessoas:
    if p[1] == max(pessoas):
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {min(pessoas)}')
for p in pessoas:
    if p[1] == min(pessoas):
        print(f'{p[0]} ', end='')
    