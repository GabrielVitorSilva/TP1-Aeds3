import random
import string
import time

class NoArvoreBinaria:
    def __init__(self, chave, dado1, dado2):
        self.chave = chave
        self.dado1 = dado1
        self.dado2 = dado2
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, dado1, dado2):
        novo_no = NoArvoreBinaria(chave, dado1, dado2)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            atual = self.raiz
            while True:
                if chave < atual.chave:
                    if atual.esquerda is None:
                        atual.esquerda = novo_no
                        break
                    atual = atual.esquerda
                elif chave > atual.chave:
                    if atual.direita is None:
                        atual.direita = novo_no
                        break
                    atual = atual.direita

    def buscar(self, chave):
        tempo_inicio = time.time()
        atual = self.raiz
        comparacoes = 0  # Inicializa o contador de comparações
        while atual is not None:
            comparacoes += 1  # Incrementa o contador a cada comparação
            if chave == atual.chave:
                tempo_fim = time.time()
                return atual, tempo_fim - tempo_inicio, comparacoes  # Retorna o nó, tempo e número de comparações
            elif chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        tempo_fim = time.time()
        return None, tempo_fim - tempo_inicio, comparacoes  # Retorna None se a chave não for encontrada

class BuscaExistentes:
    def __init__(self, arvore, num_buscas, num_entradas):
        self.arvore = arvore
        self.num_buscas = num_buscas
        self.num_entradas = num_entradas

    def buscar_numeros_existentes(self):
        resultados = []
        for _ in range(self.num_buscas):
            chave = random.choice(range(1, self.num_entradas + 1))
            resultado, tempo, comparacoes = self.arvore.buscar(chave)
            resultados.append((chave, resultado, tempo, comparacoes))  # Adiciona o número de comparações aos resultados
        return resultados

class BuscaInexistentes:
    def __init__(self, arvore, dados, num_buscas, num_entradas):
        self.arvore = arvore
        self.dados = dados
        self.num_buscas = num_buscas
        self.num_entradas = num_entradas

    def buscar_numeros_inexistentes(self):
        numeros_unicos = set(entry[0] for entry in self.dados)
        numeros_nao_encontrados = []

        while len(numeros_nao_encontrados) < self.num_buscas:
            num_aleatorio = random.randint(1, self.num_entradas * 2)
            if num_aleatorio not in numeros_unicos:
                resultado, tempo, comparacoes = self.arvore.buscar(num_aleatorio)
                if not resultado:
                    numeros_nao_encontrados.append((num_aleatorio, tempo, comparacoes))  # Adiciona o número de comparações aos resultados
        return numeros_nao_encontrados

def gerar_dados(num_entradas, ordenado=False):
    dados = []
    chaves = list(range(1, num_entradas + 1))
    if not ordenado:
        random.shuffle(chaves)

    for chave in chaves:
        dado1 = random.randint(1, 100)
        dado2 = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        dados.append((chave, dado1, dado2))
    return dados

def criar_arquivo_de_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for entrada in dados:
            arquivo.write(f"{entrada[0]} {entrada[1]} {entrada[2]}\n")

def main():
    num_entradas = int(input("Número de entradas: "))
    quantidade_buscas = int(input("Quantidade de buscas aleatórias: "))
    opcao_ordenado = input("Entradas ordenadas? (S/N): ").strip().lower()
    dados_ordenados = opcao_ordenado == 's'
    dados = gerar_dados(num_entradas, ordenado=dados_ordenados)
    criar_arquivo_de_dados(dados, 'dados.txt')

    arvore = ArvoreBinariaBusca()
    for entrada in dados:
        arvore.inserir(*entrada)

    busca_existente = BuscaExistentes(arvore, quantidade_buscas, num_entradas)
    resultados_existente = busca_existente.buscar_numeros_existentes()

    print("Busca pelos números existentes:")
    for chave, resultado, tempo, comparacoes in resultados_existente:
        if resultado:
            print(f"Chave: {chave}, encontrada, Tempo médio de busca: {tempo:.6f} segundos, Comparações: {comparacoes}")
        else:
            print(f"Chave: {chave}, não encontrada, Tempo médio de busca: {tempo:.6f} segundos, Comparações: {comparacoes}")

    input("Pressione Enter para continuar e buscar números inexistentes...")
    print()
    
    busca_nao_existente = BuscaInexistentes(arvore, dados, quantidade_buscas, num_entradas)
    resultados_nao_existente = busca_nao_existente.buscar_numeros_inexistentes()

    print("\nBusca pelos números inexistentes:")
    for chave, tempo, comparacoes in resultados_nao_existente:
        print(f"Chave: {chave}, não encontrada, Tempo médio de busca: {tempo:.6f} segundos, Comparações: {comparacoes}")

    tempo_total_existente = sum(tempo for _, _, tempo, _ in resultados_existente)
    tempo_total_nao_existente = sum(tempo for _, tempo, _ in resultados_nao_existente)

    print()
    print(f"Tempo total das buscas pelos números existentes: {tempo_total_existente:.6f} segundos")
    print(f"Tempo total das buscas pelos números inexistentes: {tempo_total_nao_existente:.6f} segundos")

if __name__ == "__main__":
    main()
