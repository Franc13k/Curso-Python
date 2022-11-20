n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))

media = (n1 + n2) / 2
print(f'Sua média foi {media}')

if media < 5:
    print(f'Sua média foi {media} e você foi reprovado!')
elif media >= 5 and media <= 6.9:
    print(f'Sua média foi {media} e você está de recuperação!')
elif media >= 7:
    print(f'Sua média foi {media} e você foi aprovado!')
