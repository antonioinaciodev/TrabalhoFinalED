from time import *
from collections import *

def carregar_arquivo(arquivo):
    palavras = []
    with open(arquivo, 'r') as f:
        palavra = f.read().split()
        for i in palavra:
            palavras.append(i)
    return palavras
            
def carregar_defdict(palavras):
    defdict = defaultdict(int)
    for palavra in palavras:
        defdict[palavra] += 1
    return defdict

def search_defdict(defdict, palavra):
    if palavra in defdict:
        print(f"A palavra '{palavra}' foi encontrada {defdict[palavra]} vez(es) no defaultdict.")
    else:
        print(f"A palavra '{palavra}' não foi encontrada no defaultdict.")

def remover_defdict(defdict, palavra):
    if palavra in defdict:
        del defdict[palavra]
        print(f"A palavra '{palavra}' foi removida do defaultdict.")
    else:
        print(f"A palavra '{palavra}' não existe no defaultdict.")

def show_defdict(defdict):
    if not defdict:
        print("O defaultdict está vazio.")
    else:
        print("Conteúdo do defaultdict:")
        for i, (palavra, count) in enumerate(defdict.items(), start=1):
            print(f"{i}: {palavra} - {count} vez(es)")

if __name__ == '__main__':
    defdict = defaultdict(int)
    arquivo = "leipzig100k.txt"
    carregado = False

    while True:
        try:
            opcao = int(input("\nEscolha uma opção: \n"
                              "1 - Carregar palavras no defaultdict\n"
                              "2 - Exibir palavras no defaultdict\n"
                              "3 - Buscar palavra no defaultdict\n"
                              "4 - Remover palavra do defaultdict\n"
                              "0 - Sair\n> "))

            if opcao == 0:
                print("Encerrando o programa!")
                break
            elif opcao == 1:
                palavras = carregar_arquivo(arquivo)
                if palavras:
                    tempo_ini = perf_counter()
                    defdict = carregar_defdict(palavras)
                    tempo_fim = perf_counter()
                    carregado = True
                    print(f"Defaultdict carregado com sucesso em {tempo_fim - tempo_ini} segundos. "
                          f"Total de palavras: {len(defdict)}")
                else:
                    print("Erro: Não foi possível carregar o arquivo.")

            elif opcao == 2:
                if carregado:
                    tempo_ini = perf_counter()
                    show_defdict(defdict)
                    tempo_fim = perf_counter()
                    print(f"Defaultdict mostrado com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O defaultdict está vazio. Carregue palavras primeiro.")
                    
            elif opcao == 3:
                if carregado:
                    palavra = input("Digite a palavra para buscar: ").strip()
                    tempo_ini = perf_counter()
                    search_defdict(defdict, palavra)
                    tempo_fim = perf_counter()
                    print(f"Palavra buscada com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O defaultdict está vazio. Carregue palavras primeiro.")
                    
            elif opcao == 4:
                if carregado:
                    palavra = input("Digite a palavra para remover: ").strip()
                    tempo_ini = perf_counter()
                    remover_defdict(defdict, palavra)
                    tempo_fim = perf_counter()
                    print(f"Palavra removida com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O defaultdict está vazio. Carregue palavras primeiro.")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")