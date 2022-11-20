from time import sleep
def maior(* num):
    print('-=' * 20)
    print(f'Todos os valores foram: {num}')
    print(f'Foram informados {len(num)} valores')
    print(f'O maior valor informado foi {max(num)}')
    sleep(2)
    
maior(1, 6, 2, 3, 7, 9, 4)
maior(15, 27, 33, 9, 1)
