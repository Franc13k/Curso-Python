nf = int(input('Digite a quantidade de elementos da sequência de Fibonacci que deseja ver: '))
n0 = 0
n1 = 1
n = 0
while n != nf:
    print(n0)
    n += 1
    if n != nf: # coloquei esse if para verificar se o  n0 printado é o ultimo termo pedido, ou não. Se for, o n1 atual não é printado.
        print(n1)
        n0 = n0 + n1
        n1 = n1 + n0
        n += 1