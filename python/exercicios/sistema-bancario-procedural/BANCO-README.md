# 🏦 Sistema Bancário em Python

Este projeto é um **simulador de operações bancárias via terminal**, desenvolvido em Python como exercício prático para aplicar os conceitos fundamentais da linguagem, como controle de fluxo, variáveis, estruturas condicionais e laços de repetição.

---

## 📋 Funcionalidades

O sistema oferece as seguintes operações:

- `[d]` **Depósito**: Permite adicionar saldo à conta.
- `[s]` **Saque**: Permite realizar saques com limite de R$500 por operação e até 3 saques por sessão.
- `[e]` **Extrato**: Mostra o saldo atual da conta e a quantidade de saques restantes.
- `[q]` **Sair**: Encerra a execução do programa.

---

## 💡 Regras de Negócio

- O valor do **saque não pode ultrapassar R$500**.
- O usuário pode realizar no **máximo 3 saques por sessão**.
- **Depósitos com valor menor ou igual a zero não são permitidos**.
- O sistema exibe mensagens de erro amigáveis para operações inválidas.

---

## 🚀 Tecnologias Utilizadas

- Linguagem: **Python 3.x**
- Execução via terminal/console

---

## 📦 Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/dio-bootcamp-santander.git
2. Acesse o diretório do projeto:

   ```bash
   cd dio-bootcamp-santander
   cd python
   cd exercicios
   cd sistema-bancario-procedural

3. Execute o programa:

   ```bash
   python sistema_banco.py

## 📄 Licença

Este projeto está sob a licença MIT.
