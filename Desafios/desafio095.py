jogadores = []
player = {}
while True:
    print('-'*70)
    soma = 0
    player["Nome"] = str(input('Nome do jogador: ')).strip().title()
    while True:
        player["Partidas"] = int(input('Quantas partidas jogou? '))
        if player["Partidas"] > 0:
            break
        print('\033[31mQuantidade deve ser maior que 0.\033[m', end=' ')
    player["GPP"] = []
    for c in range(0, player["Partidas"]):
        while True:
            gpp = int(input(f'  -> Quantos gols marcou na {c + 1}ª partida? '))
            if gpp >= 0:
                break
            print('\033[31mQuantidade não pode ser menor que zero!\033[m', end=' ')
        soma += gpp
        player["GPP"].append(gpp)
    player["GNT"] = soma
    jogadores.append(player.copy())
    player.clear()
    while True:
        r = str(input('Inserir novo jogador? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('\033[31mS para SIM ou N para não(Finalizar)!\033[m', end=' ')
    if r == 'N':
        break
print('-='*35)
print(f'\033[4m {"ID":^2} | {"Nome":^10} | {"PJ": ^3} | {"GPP":^21} | {"Saldo":^3} \033[m')
for k, p in enumerate(jogadores):
    print(f' {k:^2} | {p["Nome"]:<10} | {p["Partidas"]:^3} | {str(p["GPP"]):^21} | {p["GNT"]:^3}')
print('Legendas: PJ = Partidas jogadas | GPP = Gols por partida ')
print('-='*35)
while True:
    busca = int(input('Digite a ID para ver os dados de um jogador [999 encerra]: '))
    if busca == 999:
        print('Finalizando...')
        print('-='*35)
        break
    if busca >= len(jogadores):
        print('\033[31mJogador não localizado! \033[m', end='')
    else:
        print('=-'*35)
        print(f'Analisando temporada do jogador {jogadores[busca]["Nome"]}')
        print(f' -> {jogadores[busca]["Nome"]} jogou {jogadores[busca]["Partidas"]} '
              f'partida{"s" if jogadores[busca]["Partidas"] > 1 else ""}.')
        for i, v in enumerate(jogadores[busca]["GPP"]):
            print(f'   - Na {i+1}ª partida marcou {v} gol{"s" if v > 1 or v == 0 else ""}.')
        print(f' - Total de {jogadores[busca]["GNT"]} '
              f'gol{"s" if jogadores[busca]["GNT"] > 1 or jogadores[busca]["GNT"] == 0 else ""} na temporada.')
        print('-='*35)
print('Programa finalizado. Volte sempre!')

