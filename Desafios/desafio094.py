pessoas = dict()
dados = list()
totmul = soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Insira apenas M ou F')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    dados.append(pessoas.copy())

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
    
print(f'Foram cadastradas {len(dados)} pessoas')
media = soma / len(dados)
print(f'A média de idade é de {media:.1f} anos')
print('As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print('Pessoas que estão acima da média ', end='')
for p in dados:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
