from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'Banco.txt'
if not ArquivoExiste(arq):
    criarArquivo(arq)

while True:
    opc = menu(['Cadastrar uma pessoa', 'ver pessoas', 'Sair do sistema'])
    if opc == 1:
        nome = str(input("nome: "))
        idade = LeiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif opc == 2:
        print('Ver pessoas cadastradas')
        lerArquivo(arq)
    elif opc == 3:
        print('saindo do sistema...')
        print('Bye!')
        sleep(0.4)
        quit()
    else:
        print('\033[31mDigite apenas umas das opções!\033[m')
