# 🏦 Sistema Bancário em Python

## Descrição

Este projeto simula um sistema bancário simples em Python, com foco em práticas fundamentais da linguagem como:

- **Definição de funções com diferentes tipos de parâmetros**
- **Manipulação de listas e dicionários**
- **Organização do código no paradigma funcional (por funções)**

As funcionalidades principais incluem:

- Saque
- Depósito
- Consulta de extrato
- Cadastro de usuários
- Cadastro de contas bancárias
- Listagem de contas e usuários

---

## 💡 Objetivos do Projeto

O projeto foi desenvolvido com os seguintes objetivos:

- Praticar a definição e o uso de **parâmetros posicionais, nomeados e obrigatórios** em funções Python
- Modularizar as operações bancárias em funções bem definidas (**programação funcional**)
- Aplicar conceitos de chave única (CPF) e relacionamento entre entidades (Usuário e Conta)

---

## ⚙️ Funcionalidades

### 🔐 Cadastro de Usuário

- Informações necessárias:

  - **Nome**
  - **Data de Nascimento**
  - **CPF** (armazenado sem pontos ou traços e deve ser **único**)
  - **Endereço** no formato:  
    `logradouro, número - bairro - cidade (sigla do estado)`

- Os usuários são armazenados em uma lista.

---

### 🏦 Cadastro de Conta Corrente

- Uma conta corrente possui:

  - **Agência**: fixa "0001"
  - **Número da conta**: sequencial, iniciando em 1
  - **Usuário associado** (CPF usado como chave de busca)

- Cada usuário pode ter **mais de uma conta**, mas uma conta pertence a **apenas um usuário**.

---

### 💰 Depósito

- Recebe **apenas argumentos posicionais**:

  - `saldo`
  - `valor`
  - `extrato`

- Retorna o novo saldo e extrato atualizado.

---

### 🏧 Saque

- Recebe **apenas argumentos nomeados (keywords only)**:

  - `saldo`
  - `valor`
  - `extrato`
  - `limite`
  - `numero_saques`
  - `limite_saques`

- Retorna o novo saldo e extrato atualizado.

---

### 📄 Extrato

- Recebe argumentos **híbridos**:

  - `saldo` (posicional)
  - `extrato` (nomeado)

- Exibe o histórico de operações e o saldo atual.

---

### 📋 Listagem de Dados

- **Listar Usuários**: Exibe os usuários cadastrados e seus dados.
- **Listar Contas**: Exibe as contas criadas com número da conta, agência e CPF do usuário.

---

## 🚀 Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/dio-bootcamp-santander.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd dio-bootcamp-santander/
   cd python
   cd exercicios
   cd sistema-bancario-funcional

   ```

3. Execute o programa:

   ```bash
   python main.py
   ```

## 🧪 Exemplos de Uso

### Criar um Usuário

Nome: João Silva
Data de Nascimento: 01/01/1990
CPF: 12345678900
Endereço: Rua A, 123 - Centro - São Paulo (SP)

### Criar uma Conta

Agência: 0001
Número da Conta: 1
CPF do Titular: 12345678900

---

## 📝 Regras de Negócio

- Cada CPF pode ser cadastrado **apenas uma vez**.
- O número da conta é **gerado automaticamente** e não pode ser alterado.
- O limite de saque é controlado por valor e por quantidade de saques diários.

---

## 🎯 Tecnologias Utilizadas

- Python 3.13.5
- Paradigma: **Programação Funcional (por funções)**

---

## 🤝 Contribuições

Contribuições são bem-vindas! Fique à vontade para abrir uma issue ou enviar um pull request.

---

## 📄 Licença

Este projeto está sob a licença MIT.
