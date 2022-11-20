from math import radians, sin, cos, tan
ang = float(input('Insira o angulo que deseja: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print(f'O angulo de {ang} tem o seno de {seno}')
print(f'O angulo de {ang} tem o cosseno de {coss}')
print(f'O angulo de {ang} tem a tangente de {tang}')