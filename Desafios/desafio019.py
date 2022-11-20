import random

aluno1 = 'Davi'
aluno2 = 'Guilherme'
aluno3 = 'Ari'
aluno4 = 'Romerito'
aluno5 = 'Kauan'

print('Aluno 1 - {}' .format(aluno1))
print('Aluno 2 - {}' .format(aluno2))
print('Aluno 3 - {}' .format(aluno3))
print('Aluno 4 - {}' .format(aluno4))
print('Aluno 5 - {}' .format(aluno5))

escolha = random.randint(1, 5)

print('Aluno de numero {} foi o sorteado' .format(escolha))