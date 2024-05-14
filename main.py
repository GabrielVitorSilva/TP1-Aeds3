import random
import string
import time

class NoArvore:
    def __init__(self, chave, dado1, dado2):
        self.chave = chave
        self.dado1 = dado1
        self.dado2 = dado2
        self.esquerda = None
        self.direita = None

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, dado1, dado2):
        novo_no = NoArvore(chave, dado1, dado2)
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
        while atual is not None:
            if chave == atual.chave:
                tempo_fim = time.time()
                return atual, tempo_fim - tempo_inicio
            elif chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        tempo_fim = time.time()
        return None, tempo_fim - tempo_inicio

class BuscarNumeros:
    def __init__(self, arvore, num_buscas, num_entradas):
        self.arvore = arvore
        self.num_buscas = num_buscas
        self.num_entradas = num_entradas

    def buscar_numeros_existem(self):
        resultados = []
        for _ in range(self.num_buscas):
            chave = random.choice(range(1, self.num_entradas + 1))
            resultado, tempo = self.arvore.buscar(chave)
            resultados.append((chave, resultado, tempo))
        return resultados

class BuscarNumerosInexistentes:
    def __init__(self, arvore, dados, num_buscas, num_entradas):
        self.arvore = arvore
        self.dados = dados
        self.num_buscas = num_buscas
        self.num_entradas = num_entradas

    def buscar_numeros_nao_existem(self):
        numeros_unicos = set(entrada[0] for entrada in self.dados)
        numeros_nao_encontrados = []

        while len(numeros_nao_encontrados) < self.num_buscas:
            num_aleatorio = random.randint(1, self.num_entradas * 2)  
            if num_aleatorio not in numeros_unicos:
                resultado, tempo = self.arvore.buscar(num_aleatorio)
                if not resultado:
                    numeros_nao_encontrados.append((num_aleatorio, tempo))
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

def principal():
    num_entradas = int(input("Quantos números na árvore: "))
    quantidade_buscas = int(input("Quantidade de números para buscar: "))
    opcao_ordenado = input("Deseja ordenar os números? (S/N): ").strip().lower()
    dados_ordenados = opcao_ordenado == 's'
    dados = gerar_dados(num_entradas, ordenado=dados_ordenados)
    criar_arquivo_de_dados(dados, 'dados.txt')

    arvore = ArvoreBuscaBinaria()
    for entrada in dados:
        arvore.inserir(*entrada)

    busca_existente = BuscarNumeros(arvore, quantidade_buscas, num_entradas)
    resultados_existente = busca_existente.buscar_numeros_existem()

    print("Buscando os números existentes:")
    for chave, resultado, tempo in resultados_existente:
        if resultado:
            print(f"Número: {chave}, encontrado, Tempo médio de busca: {tempo:.6f} segundos")
        else:
            print(f"Número: {chave}, não encontrado, Tempo médio de busca: {tempo:.6f} segundos")

    input("Pressione Enter para continuar e buscar números inexistentes...")
    print()
    
    busca_nao_existente = BuscarNumerosInexistentes(arvore, dados, quantidade_buscas, num_entradas)
    resultados_nao_existente = busca_nao_existente.buscar_numeros_nao_existem()

    print("\nBuscando números inexistentes:")
    for chave, tempo in resultados_nao_existente:
        print(f"Número: {chave}, não encontrado, Tempo médio de busca: {tempo:.6f} segundos")

    tempo_total_existente = sum(tempo for _, _, tempo in resultados_existente)
    tempo_total_nao_existente = sum(tempo for _, tempo in resultados_nao_existente)

    print()
    print(f"Tempo total de busca para números existentes: {tempo_total_existente:.6f} segundos")
    print(f"Tempo total de busca para números inexistentes: {tempo_total_nao_existente:.6f} segundos")

if __name__ == "__main__":
    principal()
