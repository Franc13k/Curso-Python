sal = float(input('Insira o valor do salário'))
print(sal)

if sal > 1250:
    aum = 1250 * 0.10
    calc = (sal + aum)
    print(f'Seu salário com aumento de 10% é R${calc}')
elif sal <= 1250:
    aum1 = 1250 * 0.15
    calc1 = (sal + aum1)
    print(f'Seu salário com aumento de 15% é R${calc1}')
else:
     print('Erro! Insira um salário!')