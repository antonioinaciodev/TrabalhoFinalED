from time import *
from collections import *

def carregar_arquivo(arquivo):
    palavras = []
    with open(arquivo, 'r') as f:
        palavra = f.read().split()
        for i in palavra:
            palavras.append(i)
    return palavras
            
def carregar_na_lista(lista, palavras):
    for palavra in palavras:
        lista.append(palavra)

def search(lista, palavra):
    if palavra in lista:
        print(f"A palavra '{palavra}' foi encontrada na posição {lista.index(palavra) + 1}.")
    else:
        print(f"A palavra '{palavra}' não foi encontrada na lista.")
        
def remover(lista, palavra):
    if palavra in lista:
        lista.remove(palavra)
        print(f"A palavra '{palavra}' foi removida da lista.")
    else:
        print(f"A palavra '{palavra}' não existe na lista.")

def show(lista):
    if not lista:
        print("A lista está vazia.")
    else:
        print("Conteúdo da lista:")
        for i, palavra in enumerate(lista, start=1):
            print(f"{i}: {palavra}")



if __name__ == '__main__':
    lista = []
    arquivo = "leipzig100k.txt"
    carregado = False

    while True:
        try:
            opcao = int(input("\nEscolha uma opção: \n"
                            "1 - Carregar palavras do arquivo\n"
                            "2 - Exibir lista\n"
                            "3 - Buscar palavra na lista\n"
                            "4 - Remover palavra da lista\n"
                            "0 - Sair\n> "))

            if opcao == 0:
                print("Encerrando o programa!")
                break
            elif opcao == 1:
                palavras = carregar_arquivo(arquivo)
                if palavras:
                    tempo_ini = perf_counter()
                    carregar_na_lista(lista, palavras)
                    tempo_fim = perf_counter()
                    carregado = True
                    print(f"Arquivo carregado com sucesso em {tempo_fim - tempo_ini} segundos. "
                        f"Total de palavras: {len(palavras)}")
                    
            elif opcao == 2:
                tempo_ini = perf_counter()
                show(lista)
                tempo_fim = perf_counter()
                print(f"List mostrado com sucesso em {tempo_fim - tempo_ini} segundos. ")
                
            elif opcao == 3:
                if lista:
                    palavra = input("Digite a palavra para buscar: ").strip()
                    tempo_ini = perf_counter()
                    search(lista, palavra)
                    tempo_fim = perf_counter()
                    print(f"Palavra buscada com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("A lista está vazia. Carregue palavras primeiro.")
                    
            elif opcao == 4:
                if lista:
                    palavra = input("Digite a palavra para remover: ").strip()
                    tempo_ini = perf_counter()
                    remover(lista, palavra)
                    tempo_fim = perf_counter()
                    print(f"Palavra removida com sucesso em {tempo_fim - tempo_ini} segundos. ")
                else:
                    print("A lista está vazia. Carregue palavras primeiro.")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")