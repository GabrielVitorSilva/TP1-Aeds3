import random  # Importa o módulo random para geração de números aleatórios
import time    # Importa o módulo time para medição do tempo de execução

# Classe que define a estrutura de um registro
class Registro:
    def __init__(self, chave, dado1, dado2):
        self.chave = chave  # Chave do registro
        self.dado1 = dado1  # Primeiro dado do registro (inteiro)
        self.dado2 = dado2  # Segundo dado do registro (string)

# Classe que define a estrutura de um nó de árvore binária
class No:
    def __init__(self, registro):
        self.registro = registro  # Registro armazenado no nó
        self.esquerda = None      # Referência para o nó filho esquerdo
        self.direita = None       # Referência para o nó filho direito

# Classe que define a estrutura de uma árvore binária
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None  # Inicializa a raiz da árvore como vazia

    # Método para inserir um registro na árvore
    def inserir(self, registro):
        if not self.raiz:  # Se a árvore estiver vazia, insere o registro como raiz
            self.raiz = No(registro)
        else:
            self._inserir_recursivo(registro, self.raiz)  # Senão, insere de forma recursiva

    # Método privado para inserir um registro recursivamente na árvore
    def _inserir_recursivo(self, registro, no):
        if registro.chave < no.registro.chave:  # Se a chave do registro for menor que a do nó atual
            if not no.esquerda:                 # Se não há nó filho esquerdo, insere o registro aqui
                no.esquerda = No(registro)
            else:
                self._inserir_recursivo(registro, no.esquerda)  # Senão, insere recursivamente no filho esquerdo
        elif registro.chave > no.registro.chave:  # Se a chave do registro for maior que a do nó atual
            if not no.direita:                    # Se não há nó filho direito, insere o registro aqui
                no.direita = No(registro)
            else:
                self._inserir_recursivo(registro, no.direita)  # Senão, insere recursivamente no filho direito

# Classe que define a estrutura de uma árvore AVL
class AVL:
    def __init__(self):
        self.raiz = None  # Inicializa a raiz da árvore AVL como vazia

    # Método para inserir um registro na árvore AVL
    def inserir(self, registro):
        self.raiz = self._inserir_recursivo(registro, self.raiz)

    # Método privado para inserir um registro recursivamente na árvore AVL
    def _altura(self, no):
        if not no:
            return -1
        return no.altura

    # Métodos de rotação da árvore AVL
    def _rotacao_direita(self, no):
        nova_raiz = no.esquerda
        no.esquerda = nova_raiz.direita
        nova_raiz.direita = no
        no.altura = max(self._altura(no.esquerda), self._altura(no.direita)) + 1
        nova_raiz.altura = max(self._altura(nova_raiz.esquerda), no.altura) + 1
        return nova_raiz

    def _rotacao_esquerda(self, no):
        nova_raiz = no.direita
        no.direita = nova_raiz.esquerda
        nova_raiz.esquerda = no
        no.altura = max(self._altura(no.esquerda), self._altura(no.direita)) + 1
        nova_raiz.altura = max(self._altura(nova_raiz.direita), no.altura) + 1
        return nova_raiz

    # Método de balanceamento da árvore AVL
    def _balanceamento(self, no):
        if not no:
            return no
        if self._altura(no.esquerda) - self._altura(no.direita) > 1:
            if self._altura(no.esquerda.esquerda) >= self._altura(no.esquerda.direita):
                no = self._rotacao_direita(no)
            else:
                no.esquerda = self._rotacao_esquerda(no.esquerda)
                no = self._rotacao_direita(no)
        elif self._altura(no.direita) - self._altura(no.esquerda) > 1:
            if self._altura(no.direita.direita) >= self._altura(no.direita.esquerda):
                no = self._rotacao_esquerda(no)
            else:
                no.direita = self._rotacao_direita(no.direita)
                no = self._rotacao_esquerda(no)
        return no

    # Método privado para inserir um registro recursivamente na árvore AVL
    def _inserir_recursivo(self, registro, no):
        if not no:
            return No(registro)
        if registro.chave < no.registro.chave:
            no.esquerda = self._inserir_recursivo(registro, no.esquerda)
        elif registro.chave > no.registro.chave:
            no.direita = self._inserir_recursivo(registro, no.direita)
        else:
            return no
        no.altura = max(self._altura(no.esquerda), self._altura(no.direita)) + 1
        return self._balanceamento(no)

# Função para gerar um registro aleatório
def gerar_registro(chave):
    dado1 = random.randint(1, 100)  # Gera um número inteiro aleatório
    dado2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))  # Gera uma string aleatória de 10 caracteres
    return Registro(chave, dado1, dado2)  # Retorna o registro com os dados gerados

# Função para gerar um arquivo de dados com registros aleatórios
def gerar_arquivo(tamanho, ordenado=True):
    registros = [gerar_registro(chave) for chave in range(1, tamanho + 1)]  # Gera registros para o tamanho especificado
    if not ordenado:
        random.shuffle(registros)  # Embaralha os registros se não estiverem ordenados
    with open(f'dados_{tamanho}_{"ordenado" if ordenado else "nao_ordenado"}.txt', 'w') as arquivo:
        for registro in registros:
            arquivo.write(f"{registro.chave},{registro.dado1},{registro.dado2}\n")  # Escreve os registros no arquivo

# Função para carregar registros de um arquivo de dados
def carregar_arquivo(nome_arquivo):
    registros = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            chave, dado1, dado2 = linha.strip().split(',')  # Separa os dados da linha
            registros.append(Registro(int(chave), int(dado1), dado2))  # Adiciona o registro à lista
    return registros

# Funções de busca (não incluídas aqui para brevidade)

# Função para calcular o desempenho das buscas
def calcular_desempenho(busca, estrutura, chaves, existentes=True):
    tempos = []   # Lista para armazenar os tempos de execução das buscas
    comps = []    # Lista para armazenar o número de comparações feitas nas buscas
    for chave in chaves:
        inicio = time.time()  # Registra o tempo inicial
        resultado = busca(estrutura, chave)  # Realiza a busca
        fim = time.time()     # Registra o tempo final
        tempos.append(fim - inicio)  # Calcula o tempo de execução da busca e adiciona à lista
        comps.append(1 if resultado else 0)  # Adiciona 1 se a busca for bem-sucedida, 0 caso contrário
    tempo_medio = sum(tempos) / len(tempos)  # Calcula o tempo médio de execução das buscas
    comps_medio = sum(comps) / len(comps)    # Calcula o número médio de comparações feitas nas buscas
    return comps_medio, tempo_medio  # Retorna o número médio de comparações e o tempo médio de execução

# Gerar arquivos de dados para diferentes tamanhos e tipos (ordenado e não ordenado)
tamanhos = [100, 500, 1000, 5000, 10000]  # Lista dos tamanhos dos arquivos
for tamanho in tamanhos:
    gerar_arquivo(tamanho, ordenado=True)   # Gera arquivo ordenado
    gerar_arquivo(tamanho, ordenado=False)  # Gera arquivo não ordenado

# Carregar arquivos e realizar buscas
chaves_busca = [random.randint(1, 1000) for _ in range(15)]            # Gera 15 chaves de busca aleatórias
chaves_nao_presentes = [random.randint(1001, 2000) for _ in range(15)]  # Gera 15 chaves que não estão nos registros
resultados = []  # Lista para armazenar os resultados das análises de desempenho

for tamanho in tamanhos:
    for ordenado in [True, False]:
        arquivo = f'dados_{tamanho}_{"ordenado" if ordenado else "nao_ordenado"}.txt'  # Determina o nome do arquivo a ser carregado
        registros = carregar_arquivo(arquivo)  # Carrega os registros do arquivo
        estrutura_sequencial = registros       # Estrutura sequencial é simplesmente uma lista de registros
        arvore_binaria = ArvoreBinaria()       # Inicializa uma árvore binária vazia
        avl = AVL()                            # Inicializa uma árvore AVL vazia
        for registro in registros:             # Insere os registros nas estruturas de dados
            arvore_binaria.inserir(registro)   # Insere na árvore binária
            avl.inserir(registro)              # Insere na árvore AVL
        # Calcula o desempenho das buscas para cada tipo de estrutura e tipo de busca (presente e não presente)
        comps_seq_presente, tempo_seq_presente = calcular_desempenho(busca_sequencial, estrutura_sequencial, chaves_busca)
        comps_seq_nao_presente, tempo_seq_nao_presente = calcular_desempenho(busca_sequencial, estrutura_sequencial, chaves_nao_presentes, existentes=False)
        comps_bin_presente, tempo_bin_presente = calcular_desempenho(busca_arvore_binaria, arvore_binaria, chaves_busca)
        comps_bin_nao_presente, tempo_bin_nao_presente = calcular_desempenho(busca_arvore_binaria, arvore_binaria, chaves_nao_presentes, existentes=False)
        comps_avl_presente, tempo_avl_presente = calcular_desempenho(busca_avl, avl, chaves_busca)
        comps_avl_nao_presente, tempo_avl_nao_presente = calcular_desempenho(busca_avl, avl, chaves_nao_presentes, existentes=False)
        # Adiciona os resultados à lista de resultados
        resultados.append((tamanho, ordenado, comps_seq_presente, tempo_seq_presente, comps_seq_nao_presente, tempo_seq_nao_presente, comps_bin_presente, tempo_bin_presente, comps_bin_nao_presente, tempo_bin_nao_presente, comps_avl_presente, tempo_avl_presente, comps_avl_nao_presente, tempo_avl_nao_presente))

# Exibir resultados
print("Tam. Ordenado CompSeqP TempoSeqP CompSeqNP TempoSeqNP CompBinP TempoBinP CompBinNP TempoBinNP CompAVLP TempoAVLP CompAVLNP TempoAVLNP")
for resultado in resultados:
    print(*resultado)
