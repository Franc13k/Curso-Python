times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
         'Athletico-PR', 'AméricaMG', 'Atlético-MG', 'SãoPaulo', 'Botafogo',
         'Fortaleza', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
         'Cuiabá', 'Athletico-GO', 'Ceará SC', 'Avaí', 'Juventude')
ordeAlfa = sorted(times)

print(f'Os 5 primeiros colocados do brasileirão são: {times[0:5]}')
print(f'Os 4 últimos colocados do brasileirão são: {times[16:20]}')
print(f'Os times em ordem alfabética são: {ordeAlfa}')
print(f'O Coritiba está na {times.index("Coritiba")} posição')
