jogador = dict()
jogador['Nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Total de partidas jogadas: '))
jogador['gols'] = float(input('Média de gols por partida: '))
jogador['totgols'] = jogador['partidas'] * jogador['gols']

for k, v in jogador.items():
    print(f'{k} tem o valor de {v}')
