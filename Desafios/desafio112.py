def leiadinheiro(v):
    while True:
        x = str(input(v)).strip()
        copy = x.replace('ponto', 'vírgula').split('vírgula')
        if 'vírgula' in x:
            x = x.replace('vírgula', 'ponto')
            if copy[0].isnumeric() is True and copy[1].isnumeric() is True:
                return float(x)
            else:
                print(f'\033[31mERRO! "{x}" é um preço incorreto.\033[0m')
        else:
            if copy[0].isnumeric() is True:
                return float(x)
            else:
                print(f'\033[31mERRO! "{x}" é um preço incorreto.\033[0m')