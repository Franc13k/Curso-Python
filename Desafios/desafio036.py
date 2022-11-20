casa = float(input('Insira o valor da casa:'))
sal = int(input('Insira o salário:'))
anos = int(input('Em quantos anos vai pagar?'))

print(f'Valor da casa: R${casa}')
print(f'Salário: R${sal}')
print(f'Anos que deseja pagar a casa: {anos}')
meses = anos * 12
parcela = casa / meses
porcent = sal * 0.30

if parcela <= porcent:
    print(f'O valor da parcela é {parcela}')
elif parcela > porcent:
    print('Parcela maior que 30''%'' do salário ') 
