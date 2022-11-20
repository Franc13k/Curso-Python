d = int(input('Insira os dias que passou alugado: '))
km = float(input('Insira os km rodados: '))
pago = (d*60) + (km*0.15)
print(f'O total é R${pago}')