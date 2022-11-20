lista = []
p1 = 'S'
while p1 in 'Ss':
    num = int(input('Digite um numero : '))
    p1 = input('Quer continuar ? [S/N]').strip().upper()
    lista.append(num)
    if p1 == 'N':
        break
print(f'Você digitou {len(lista)} numeros e a media foi {sum(lista) / len(lista)} \n O maior valor foi {max(lista)} e o menor foi {min(lista)}')