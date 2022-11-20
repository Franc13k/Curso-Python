pessoas = {}
pessoas['nome'] = str(input('Insira o nome do aluno: '))
pessoas['media'] = float(input('Insira a média do aluno: '))

print(f'Nome é {pessoas["nome"]}')
print(f'Média é {pessoas["media"]}')

if pessoas["media"] >= 6:
    print('Situação é Aprovado')
else:
    print('Situação é Reprovado')
    

