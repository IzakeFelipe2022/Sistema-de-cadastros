def linha(tam=42):
    return tam*'-'


def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('Erro de valor!!')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return num

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for opcoes in lista:
        print(f'\033[33m{c}\033[m ==> \033[34m {opcoes}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('Digite uma opção: ')
    return opc



if __name__ == '__main__':
 pass








