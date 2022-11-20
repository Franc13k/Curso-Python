from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'menu.txt'

if not arqExiste(arq):
    criarArquivo(arq)
    
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)
