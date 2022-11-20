alt = float(input('Insira sua altura em metros: '))
peso = float(input('Insira seu peso em kilogramas: '))

quad = alt * alt
imc = peso / quad

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Você está no peso ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

