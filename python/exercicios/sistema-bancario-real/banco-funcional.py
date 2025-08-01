from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime       
     
class Cliente:
    def __init__(self,endereco):
        self._endereco = str(endereco)
        self._contas = []
        
    def realizarTransacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionarConta(self, conta):
        self.contas.append(conta)
  
class PessoaFisica(Cliente):
    def __init__(self,nome,cpf,data_nascimento,endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento  

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(self, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        saldo = self,saldo
        excedeu_saldo = valor > saldo
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")   
            return True
            
        else:
            print("\n@@@ Operação Falhou. O valor informado é inválido. @@@")    
            
        return False
    
    def deposito(self,valor):
        if valor > 0:
            self._saldo += valor
            print(f"=== Operação concluída!===")    
        else:
            print("@@@ Operação Falhou. Não é possível  depositar valores abaixo de zero.@@@")
            return False
        return True
    
class ContaCorrente(Conta):
    def __init__(self,numero,cliente, limite=500,limite_saques=3):
        super().__init__(numero,cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        
        def sacar(self,valor):
            numero_saques = len(
                [transacao for transacao in self.historico.transacoes if transacao ["tipo"] == Saque.__name__]
            )
            
            excedeu_limite = valor > self.limite
            excedeu_saques = numero_saques >= self.limite_saques
            
            if excedeu_limite:
                print("\n@@@ Operação falhou! O valor de saque excede o limite. @@@")
                
            elif excedeu_saques:
                print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
                
            else:
                return super().sacar(valor)
            
            return False

        def __str__(self):
            return f"""\
                Agência: \t {self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self.cliente.nome}
                """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):        
        return self._transacao
        
    def adicionarTransacao(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y %h:%m:%s"),
            }
        )

       
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self,conta):
        pass
            
class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)