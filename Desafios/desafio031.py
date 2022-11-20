distancia = int(input('Qual a distancia da viagem?'))

if distancia <= 200:
    calc = distancia * 0.50
    print(f'O preço da sua viagem é {calc}')
else:
    calc2 = distancia * 0.45
    print(f'O preço da sua viagem é {calc2}')