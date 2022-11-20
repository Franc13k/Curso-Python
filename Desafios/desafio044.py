valor = float(input('Insira o valor do produto: '))
pag = int(input("""--- Insira a forma de pagamento ---
                        1- Dinheiro/Cheque - 10% Desconto
                        2- Cartão - 5% Desconto
                        3- Cartão - 2x
                        4- Cartão - 3x 20% Juros
                        """))

descdin = valor * 0.10
desc1 = valor - descdin

descart = valor * 0.05
desc2 = valor - descart

juros = valor * 0.20
valjuros = valor + juros

if pag == 1:
    print(f'Desconto de 10% o produto ficou de {valor} por {desc1}')
    
elif pag == 2:
    print(f'Desconto de 5% o produto ficou de {valor} por {desc2}') 
    
elif pag == 3:
    print(f'Sem descontos o produto ficou pelo preço normal de {valor}')    

elif pag == 4:
    print(f'20% de Juros o produto ficou de {valor} por {valjuros}')
    