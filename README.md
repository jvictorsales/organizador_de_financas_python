# 💰 Organizador de Finanças (CLI)

Um aplicativo simples de **organização de finanças pessoais no terminal**, desenvolvido em **Python**, permitindo registrar ganhos, gastos e acompanhar o saldo atual.

Este projeto foi criado como prática de programação e aprendizado de conceitos fundamentais de Python, como manipulação de arquivos, estruturas de dados e organização de código.

---

## 📌 Funcionalidades

* Registrar **ganhos**
* Registrar **gastos**
* Listar todas as **transações**
* Calcular e exibir o **saldo atual**
* Persistência de dados utilizando **JSON**

---

## 🧠 Conceitos de Python utilizados

Este projeto utiliza diversos conceitos importantes da linguagem:

* Funções
* Listas e dicionários
* Manipulação de arquivos
* Uso do módulo `json`
* Tratamento de exceções (`try/except`)
* Estruturas de repetição (`while`, `for`)
* Validação de entrada do usuário
* Separação de responsabilidades entre funções

---

## 📂 Estrutura do projeto

```
organizador-financas/
│
├── main.py
├── transacoes.json
└── README.md
```

---

## ▶️ Como executar o projeto

1. Clone o repositório:

```
git clone https://github.com/jvictorsales/organizador_de_financas_python.git
```

2. Entre na pasta do projeto:

```
cd NOME_DO_REPOSITORIO
```

3. Execute o programa:

```
python main.py
```

---

## 📋 Exemplo de uso

```
===== ORGANIZADOR DE FINANÇAS =====

1 - Registrar ganho
2 - Registrar gasto
3 - Listar transações
4 - Ver saldo
0 - Sair
```

Exemplo de saída:

```
===== TRANSAÇÕES =====

ganho | 3000 | salario  | 2026-03-07
gasto | 50   | lanche   | 2026-03-07
gasto | 120  | internet | 2026-03-06
```

---

## 💾 Armazenamento de dados

As transações são armazenadas em um arquivo **JSON** (`transacoes.json`).

Cada transação possui a seguinte estrutura:

```json
{
  "tipo": "gasto",
  "valor": 50.0,
  "descricao": "lanche",
  "data": "2026-03-07"
}
```

---

## 🚀 Possíveis melhorias futuras

Algumas funcionalidades que podem ser adicionadas em versões futuras:

* Categorias de gastos
* Filtros de transações
* Relatórios mensais
* Gráficos de gastos
* Suporte a banco de dados (SQLite)
* Interface gráfica ou versão web

---

## 👨‍💻 Autor

Projeto desenvolvido por **João Sales** como parte do aprendizado em Python.
