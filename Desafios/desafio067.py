n = 0
while True:
    n = int(input('Deseja ver a tabuada de qual numero? '))
    if n < 0:
        break
    por1 = n * 1
    por2 = n * 2
    por3 = n * 3
    por4 = n * 4
    por5 = n * 5
    por6 = n * 6
    por7 = n * 7
    por8 = n * 8
    por9 = n * 9
    por10 = n * 10
    print(f'-------- Tabuada do {n} --------')
    print(f'{n} x 1 = {por1}')
    print(f'{n} x 2 = {por2}')
    print(f'{n} x 3 = {por3}')
    print(f'{n} x 4 = {por4}')
    print(f'{n} x 5 = {por5}')
    print(f'{n} x 6 = {por6}')
    print(f'{n} x 7 = {por7}')
    print(f'{n} x 8 = {por8}')
    print(f'{n} x 9 = {por9}')
    print(f'{n} x 10 = {por10}')
    
    
    '''
    RESOLUÇÃO FÁCIL
    while True:
        n = int(input('Deseja ver tabuada de qual numero?'))
        print('-' * 30)
        if n < 0
            break
        for c in range(1,11):
            print(f'{n} x {c} = {n*c}')
        print('-' * 30)
    print('Programa encerrado!')
    '''
    