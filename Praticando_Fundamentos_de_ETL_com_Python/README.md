# ETL Challenge - Processamento de Dados

Este projeto faz parte de um conjunto de desafios de ETL (Extract, Transform, Load), com foco em manipulação de dados de entrada simples para geração de saídas padronizadas. O objetivo é praticar transformação de dados utilizando apenas recursos básicos da linguagem, sem bibliotecas externas.

---

## 🧩 Desafio 1 - Cálculo de Venda de Produtos

### 📌 Descrição

Você deve implementar um programa que processa dados de vendas de produtos. Cada entrada contém o nome do produto, a quantidade vendida e o valor unitário.

O sistema deve:

- Extrair os dados da entrada
- Calcular o valor total da venda (quantidade × valor unitário)
- Retornar o resultado formatado

### 📥 Entrada

Uma única linha contendo:

produto,quantidade,valor_unitario

- produto → string
- quantidade → inteiro
- valor_unitario → inteiro

### 📤 Saída

Uma string no formato:

produto: total

Onde total = quantidade * valor_unitario.

### 🧪 Exemplos

Entrada | Saída
--- | ---
caneta,10,2 | caneta: 20
caderno,5,7 | caderno: 35
lapis,0,3 | lapis: 0
borracha,3,0 | borracha: 0

---

## 🧩 Desafio 2 - Padronização de Nomes de Clientes

### 📌 Descrição

Você deve criar um programa que padroniza nomes de clientes recebidos em uma única linha.

O sistema deve:

- Separar os nomes por vírgula
- Remover espaços extras antes e depois de cada nome
- Converter todos os nomes para letras maiúsculas
- Reunir os nomes no formato padronizado

### 📥 Entrada

Uma única linha contendo nomes separados por vírgula:

nome1, nome2, nome3

Os nomes podem conter espaços extras.

### 📤 Saída

Uma única linha com os nomes:

- Em letras maiúsculas
- Sem espaços extras
- Separados por "; "

### 🧪 Exemplos

Entrada | Saída
--- | ---
ana, bruno, carla | ANA; BRUNO; CARLA
lucas , maria ,joao | LUCAS; MARIA; JOAO
paulo, sofia | PAULO; SOFIA
alice | ALICE

---

## ⚙️ Regras Gerais

- Não utilizar bibliotecas externas
- Utilizar apenas recursos padrão da linguagem
- A entrada sempre será uma única linha
- A saída deve seguir exatamente o formato especificado

---

## 🚀 Objetivo

Desenvolver habilidades em:

- Manipulação de strings
- Transformação de dados
- Lógica de programação
- Construção de ETL simples (Extract, Transform, Load)
