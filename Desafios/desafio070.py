totGas = qntPro = menor = cont = 0
barato = ''
while True:
    nome = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: '))
    totGas += preco
    cont += 1
    
    if preco > 1000:
        qntPro += 1

    if cont == 1 or preco < menor: #se o contador for o primeiro produto ou preco menor que o menor preco
        menor = preco #o menor preço passa a ser o preço
        barato = nome
    #else:
        #if preco < menor: se o preço for menor, doq o menor preço
           # menor = preco
            #barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
    
print(f'O total das compras foi R${totGas:.2f}')
print(f'{qntPro} produtos custam mais de R$1000')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
    