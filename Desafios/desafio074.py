from random import sample

num = tuple(sample(range(101),5))


print(f'Os 5 números gerados de 0 a 100 foram {num}')
print(f'O menor número foi {min(num)}')
print(f'O maior número foi {max(num)}')

