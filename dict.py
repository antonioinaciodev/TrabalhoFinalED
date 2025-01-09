from time import *
from collections import *

def carregar_arquivo(arquivo):
    palavras = []
    with open(arquivo, 'r') as f:
        palavra = f.read().split()
        for i in palavra:
            palavras.append(i)
    return palavras
            
def carregar_dict(palavras):
    dict_palavras = {}
    for palavra in palavras:
        dict_palavras[palavra] = None
    return dict_palavras

def search_dict(dict_palavras, palavra):
    if palavra in dict_palavras:
        print(f"A palavra '{palavra}' foi encontrada no dicionário.")
    else:
        print(f"A palavra '{palavra}' não foi encontrada no dicionário.")

def remover_dict(dict_palavras, palavra):
    if palavra in dict_palavras:
        del dict_palavras[palavra]
        print(f"A palavra '{palavra}' foi removida do dicionário.")
    else:
        print(f"A palavra '{palavra}' não existe no dicionário.")

def show_dict(dict_palavras):
    if not dict_palavras:
        print("O dicionário está vazio.")
    else:
        print("Conteúdo do dicionário:")
        for i, palavra in enumerate(dict_palavras.keys(), start=1):
            print(f"{i}: {palavra}")

if __name__ == '__main__':
    dict_palavras = {}
    arquivo = "leipzig100k.txt"
    carregado = False

    while True:
        try:
            opcao = int(input("\nEscolha uma opção: \n"
                              "1 - Carregar palavras no dicionário\n"
                              "2 - Exibir palavras no dicionário\n"
                              "3 - Buscar palavra no dicionário\n"
                              "4 - Remover palavra do dicionário\n"
                              ""
                              "0 - Sair\n> "))

            if opcao == 0:
                print("Encerrando o programa!")
                break
            elif opcao == 1:
                palavras = carregar_arquivo(arquivo)
                if palavras:
                    tempo_ini = perf_counter()
                    dict_palavras = carregar_dict(palavras)
                    tempo_fim = perf_counter()
                    carregado = True
                    print(f"Dict carregado com sucesso em {tempo_fim - tempo_ini} segundos. "
                          f"Total de palavras: {len(dict_palavras)}")

            elif opcao == 2:
                tempo_ini = perf_counter()
                show_dict(dict_palavras)
                tempo_fim = perf_counter()
                print(f"Dict mostrado com sucesso em {tempo_fim - tempo_ini} segundos. ")
                
            elif opcao == 3:
                if carregado:
                    palavra = input("Digite a palavra para buscar: ").strip()
                    tempo_ini = perf_counter()
                    search_dict(dict_palavras, palavra)
                    tempo_fim = perf_counter()
                    print(f"Palavra buscada com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O dicionário está vazio. Carregue palavras primeiro.")
                    
            elif opcao == 4:
                if carregado:
                    palavra = input("Digite a palavra para remover: ").strip()
                    tempo_ini = perf_counter()
                    remover_dict(dict_palavras, palavra)
                    tempo_fim = perf_counter()
                    print(f"Palavra removida com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("O dicionário está vazio. Carregue palavras primeiro.")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")