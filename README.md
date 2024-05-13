Busca e Análise de Desempenho em Estruturas de Dados
Este projeto consiste em uma implementação de estruturas de dados (árvore binária e árvore AVL) e uma análise de desempenho de algoritmos de busca nessas estruturas.

Como Executar
Certifique-se de ter o Python 3 instalado em seu sistema. Você pode baixá-lo aqui.

Clone este repositório para o seu ambiente local:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Navegue até o diretório do projeto:

arduino
Copiar código
cd nome-do-repositorio
Execute o script Python main.py:

css
Copiar código
python3 main.py
O script irá gerar arquivos de dados com registros aleatórios, realizar operações de busca em diferentes estruturas de dados e registrar o desempenho das buscas em um arquivo de saída.

Como Funciona
O código é dividido em várias partes:

Estruturas de Dados: Implementação de uma árvore binária e uma árvore AVL, com métodos para inserção de registros.
Geração de Dados: Funções para gerar registros aleatórios e criar arquivos de dados com esses registros.
Carregamento de Dados: Função para carregar registros de arquivos de dados.
Busca e Análise de Desempenho: Funções para calcular o desempenho de operações de busca em diferentes estruturas de dados.
O script principal (main.py) realiza as seguintes operações:

Gera arquivos de dados com registros aleatórios de diferentes tamanhos e tipos (ordenados e não ordenados).
Carrega os registros dos arquivos de dados.
Insere os registros em estruturas de dados (árvore binária e árvore AVL).
Realiza operações de busca em cada estrutura de dados.
Calcula o desempenho das buscas (número médio de comparações e tempo médio de execução).
Registra os resultados da análise de desempenho em um arquivo de saída.
