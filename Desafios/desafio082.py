valores = []
par = []
impar = []
while True:
    valores.append(int(input('Insira o valor: ')))
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break

for i, v in enumerate(valores):
    if (v % 2) == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Os valores digitados foram {valores}')
print(f'Os valores impares foram {impar}')
print(f'Os valores pares foram {par}')
