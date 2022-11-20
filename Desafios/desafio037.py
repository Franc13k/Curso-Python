import opcode


num = int(input('Insira um número inteiro:'))
opcao = int(input("""--- Escolha uma opção ---
                    1- Converter para binário
                    2- Converter para octal
                    3- Converter para hexadecimal"""))

binario = format(num, "b")
octal = format(num, "o")
hexa = format(num, "x")
if opcao == 1:
    print('O numero escolhido foi transformado em binário')
    print(f'{binario}')
elif opcao == 2:
    print('O número escolhido foi transfomardo para octal')
    print(f'{octal}')
elif opcao == 3:
    print('O número escolhido foi transformado para hexadecimal')
    print(f'{hexa}')