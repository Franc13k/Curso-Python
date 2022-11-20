def aumentar(preco = 0, taxa = 0, format = False):
    s = preco + (preco * taxa/100)
    return s if format is False else moeda(s)

def diminuir(preco = 0, taxa = 0, format = False):
    s = preco - (preco * taxa/100)
    return s if format is False else moeda(s)


def dobro(preco = 0, format = False):
    s = preco * 2
    return s if format is False else moeda(s)


def metade(preco = 0, format = False):
    s = preco / 2
    return s if format is False else moeda(s)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco=0, taxaa=10, taxad=5):
    print(f'=-' * 30)
    print(f'RESUMO DO VALOR')
    print(f'=-' * 30)
    print(f'Preço inserido: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'80% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'35% de redução: \t{diminuir(preco, taxad, True)}')