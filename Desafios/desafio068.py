from random import randint

quant= 0
while True:
    pc = randint(0,11)
    num = int(input('Digite um valor  '))
    total = pc + num
    resultado = ['par' if total % 2 == 0 else 'impar']
    palpite =' '

    while palpite not in 'PI':
        palpite = str(input('P/I ?')).strip().upper()[0]
    if palpite =='P' and resultado[0] == 'par':
        quant+=1
        print(f'Venceu!!!  Você jogou {num} e o computador {pc}. Total de {total}, deu {resultado[0]}')
    elif palpite == 'I' and resultado[0] =='impar':
        print(f'Venceu!!!  Você jogou {num} e o computador {pc}. Total de {total}, deu {resultado[0]}')
        quant+=1
    else:
        print(f'Você perdeu!  Pc jogou {pc} , vc {num}. Total {total}, {resultado[0]}')
        break
    print('Vamos jogar novamente...')
print(f'GAME OVER!, você venceu {quant} vezes.')