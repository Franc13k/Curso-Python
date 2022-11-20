tot18 = 0
qnthom = 0
qntmul = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: M/F ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
        
    if sexo == 'M':
        qnthom += 1
    
    if sexo == 'F' & idade < 20:
        qntmul += 1
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{tot18} pessoas maior de idade')
print(f'{qnthom} homens foram cadastrados')
print(f'{qntmul} mulheres com menos de 20 anos')