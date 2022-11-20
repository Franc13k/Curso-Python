total_idade = 0
listan = []
listai = []
m20 = 0
for c in range(1, 5):
    print(f"------ {c}° PESSOA -------")
    nome = str(input("Qual é seu nome? ")).strip().title()
    idade = int(input("Idade: "))
    total_idade += idade
    Sexo = int(input("""Digite [1] para sexo masculino e
Digite [2] para sexo feminino:"""))
    if Sexo == 1:
        listan.append(nome)
        listai.append(idade)
    if Sexo == 2 and idade < 20:
        m20 += 1
print(f"A idade média do grupo é {total_idade / 4:.2f} anos")
print(f"O homem mais velho tem {max(listai)} anos e seu nome é {listan[listai.index(max(listai))]}")
print(f'E no total {m20} mulheres tem menos de 20 anos. ')