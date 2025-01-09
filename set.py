from time import *
from collections import *

def carregar_arquivo(arquivo):
    palavras = []
    with open(arquivo, 'r') as f:
        palavra = f.read().split()
        for i in palavra:
            palavras.append(i)
    return palavras
            
def carregar_conjunto(palavras):
    conjunto = set()
    for palavra in palavras:
        conjunto.add(palavra)
    return conjunto

def search_conjunto(conjunto, palavra):
    if palavra in conjunto:
        print(f"A palavra '{palavra}' foi encontrada no conjunto.")
    else:
        print(f"A palavra '{palavra}' não foi encontrada no conjunto.")

def remover_conjunto(conjunto, palavra):
    if palavra in conjunto:
        conjunto.remove(palavra)
        print(f"A palavra '{palavra}' foi removida do conjunto.")
    else:
        print(f"A palavra '{palavra}' não existe no conjunto.")

def show_conjunto(conjunto):
    if not conjunto:
        print("O conjunto está vazio.")
    else:
        print("Conteúdo do conjunto:")
        for i, palavra in enumerate(conjunto, start=1):
            print(f"{i}: {palavra}")

if __name__ == '__main__':
    conjunto = set()
    arquivo = "leipzig100k.txt"
    carregado = False

    while True:
        try:
            opcao = int(input("\nEscolha uma opção: \n"
                              "1 - Carregar palavras no conjunto\n"
                              "2 - Exibir palavras no conjunto\n"
                              "3 - Buscar palavra no conjunto\n"
                              "4 - Remover palavra do conjunto\n"
                              "0 - Sair\n> "))

            if opcao == 0:
                print("Encerrando o programa!")
                break
            
            elif opcao == 1:
                palavras = carregar_arquivo(arquivo)
                if palavras:
                    tempo_ini = perf_counter()
                    conjunto = carregar_conjunto(palavras)
                    tempo_fim = perf_counter()
                    carregado = True
                    print(f"Conjunto carregado com sucesso em {tempo_fim - tempo_ini} segundos. "
                          f"Total de palavras: {len(conjunto)}")
                else:
                    print("Erro: Não foi possível carregar o arquivo.")

            elif opcao == 2:
                if carregado:
                    tempo_ini = perf_counter()
                    show_conjunto(conjunto)
                    tempo_fim = perf_counter()
                    print(f"Set mostrado com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O conjunto está vazio. Carregue palavras primeiro.")
                    
            elif opcao == 3:
                if carregado:
                    palavra = input("Digite a palavra para buscar: ").strip()
                    tempo_ini = perf_counter()
                    search_conjunto(conjunto, palavra)
                    tempo_fim = perf_counter()
                    print(f"Palavra buscada com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O conjunto está vazio. Carregue palavras primeiro.")
            elif opcao == 4:
                if carregado:
                    palavra = input("Digite a palavra para remover: ").strip()
                    tempo_ini = perf_counter()
                    remover_conjunto(conjunto, palavra)
                    tempo_fim = perf_counter()
                    print(f"Palavra removida com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O conjunto está vazio. Carregue palavras primeiro.")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")