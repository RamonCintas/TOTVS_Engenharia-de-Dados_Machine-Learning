# README.md — Desafios de Lógica (1 e 2)

Este repositório contém dois desafios de programação voltados para lógica, controle de fluxo e manipulação de entradas numéricas e textuais. O objetivo é praticar resolução de problemas comuns em sistemas de automação empresarial.

---

## 🚀 Desafio 1 — Cálculo de Desconto em Pedido

### 📌 Descrição
Você deve desenvolver um programa que calcula o valor final de um pedido após a aplicação de um desconto percentual. O sistema é utilizado para automatizar cálculos em larga escala, garantindo precisão e reduzindo erros humanos.

### 📥 Entrada
Uma única linha contendo:
- Um número decimal positivo representando o valor total do pedido
- Um número inteiro entre 0 e 100 representando o percentual de desconto

Exemplo:
```
150.00 10
```

### 📤 Saída
O valor final do pedido após o desconto, com **duas casas decimais**.

### ⚙️ Regra de cálculo
```
valor_final = valor_total - (valor_total * desconto / 100)
```

### 🧾 Exemplos
| Entrada        | Saída   |
|---------------|---------|
| 150.00 10     | 135.00  |
| 200.50 25     | 150.38  |
| 99.99 0       | 99.99   |
| 80.00 100     | 0.00    |

---

## 🚀 Desafio 2 — Sistema de Aprovação de Pedidos

### 📌 Descrição
Você deve implementar uma lógica de decisão para aprovar, revisar ou rejeitar pedidos com base no valor e na prioridade. Esse sistema automatiza decisões simples de negócios.

### 📥 Entrada
Uma única linha contendo:
- Um número inteiro representando o valor do pedido
- Uma string representando a prioridade (`"alta"`, `"media"` ou `"baixa"`)

Exemplo:
```
800 alta
```

### 📤 Saída
Uma única palavra:
- `aprovado`
- `revisao`
- `rejeitado`

### ⚙️ Regras de decisão
- Pedidos com valor **até 1000** e prioridade **alta ou media** → `aprovado`
- Pedidos com valor **acima de 1000** e prioridade **alta** → `revisao`
- Todos os demais casos → `rejeitado`

### 🧾 Exemplos
| Entrada        | Saída      |
|---------------|------------|
| 800 alta      | aprovado   |
| 1200 alta     | revisao    |
| 500 baixa     | rejeitado  |
| 1500 media    | aprovado   |

---

## 🧠 Objetivo
Praticar:
- Leitura de entrada
- Operações matemáticas simples
- Estruturas condicionais (if/else)
- Regras de negócio

---

## 📌 Observações
- Não utilizar bibliotecas externas para cálculos ou formatação.
- A saída deve seguir exatamente o formato especificado.
- Foque na precisão e na lógica de decisão.

---

## 📂 Estrutura sugerida
```
/
├── desafio1.py
├── desafio2.py
└── README.md
```

---