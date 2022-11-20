vel = int(input('Qual a velocidade do seu carro?'))

if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi multado em {multa}')
else:
    print('Parabéns, você não está acima da velocidade máxima')