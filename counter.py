from time import *
from collections import *

def carregar_arquivo(arquivo):
    palavras = []
    with open(arquivo, 'r') as f:
        palavra = f.read().split()
        for i in palavra:
            palavras.append(i)
    return palavras
            
def carregar_counter(palavras):
    counter = Counter()
    counter.update(palavras)
    return counter

def search_counter(counter, palavra):
    if palavra in counter:
        print(f"A palavra '{palavra}' foi encontrada {counter[palavra]} vez(es) no Counter.")
    else:
        print(f"A palavra '{palavra}' não foi encontrada no Counter.")

def remover_counter(counter, palavra):
    if palavra in counter:
        del counter[palavra]
        print(f"A palavra '{palavra}' foi removida do Counter.")
    else:
        print(f"A palavra '{palavra}' não existe no Counter.")

def show_counter(counter):
    if not counter:
        print("O Counter está vazio.")
    else:
        print("Conteúdo do Counter:")
        for i, (palavra, count) in enumerate(counter.items(), start=1):
            print(f"{i}: {palavra} - {count} vez(es)")

if __name__ == '__main__':
    counter = Counter()
    arquivo = "leipzig100k.txt"
    carregado = False

    while True:
        try:
            opcao = int(input("\nEscolha uma opção: \n"
                              "1 - Carregar palavras no Counter\n"
                              "2 - Exibir palavras no Counter\n"
                              "3 - Buscar palavra no Counter\n"
                              "4 - Remover palavra do Counter\n"
                              "0 - Sair\n> "))

            if opcao == 0:
                print("Encerrando o programa!")
                break
            elif opcao == 1:
                palavras = carregar_arquivo(arquivo)
                if palavras:
                    tempo_ini = perf_counter()
                    counter = carregar_counter(palavras)
                    tempo_fim = perf_counter()
                    carregado = True
                    print(f"Counter carregado com sucesso em {tempo_fim - tempo_ini} segundos. "
                          f"Total de palavras: {len(counter)}")
                else:
                    print("Erro: Não foi possível carregar o arquivo.")

            elif opcao == 2:
                if carregado:
                    tempo_ini = perf_counter()
                    show_counter(counter)
                    tempo_fim = perf_counter()
                    print(f"Counter mostrado com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O Counter está vazio. Carregue palavras primeiro.")
                    
            elif opcao == 3:
                if carregado:
                    palavra = input("Digite a palavra para buscar: ").strip()
                    tempo_ini = perf_counter()
                    search_counter(counter, palavra)
                    tempo_fim = perf_counter()
                    print(f"Palavra buscada com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O Counter está vazio. Carregue palavras primeiro.")
                    
            elif opcao == 4:
                if carregado:
                    palavra = input("Digite a palavra para remover: ").strip()
                    tempo_ini = perf_counter()
                    remover_counter(counter, palavra)
                    tempo_fim = perf_counter()
                    print(f"Palavra removida com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O Counter está vazio. Carregue palavras primeiro.")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")