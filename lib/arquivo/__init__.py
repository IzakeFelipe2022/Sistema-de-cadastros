def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f"Arquivo criado {nome} com sucesso!")

def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao abrir arquivo!')
    else:
        idade = ''
        nome = ''
        for linha in a:
                dado = linha.split(':')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[1].upper():.<30} {dado[0]:>3} anos')



def cadastrar(arq, idade = 0, nome = "desconnhecido"):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Nõa foi possível abrir arquivo!')
    else:
        try:
            arquivo.write(f'{nome}:{idade}\n')
        except:
            print('Não foi possível gravar os dados informados')
        else:
            print('Dados gravados com sucesso!')
            arquivo.close()

