class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia 
        self.conta = conta
        self.saldo = saldo
        self.historico = ''
        self.limite_saque = 500
        self.limite_qtd_saque = 3

    def __str__(self):
        return f'Agencia: {self.agencia}\nConta: {self.conta}\nSaldo: {self.saldo:.2f}'
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico += f'Deposito de R$ {valor:.2f}\n'
            return ('Deposito efetuado com sucesso.')
        else:
            return ('Deposito inválido. Tente novamente.')    
    
    def sacar(self, valor):
        if valor > self.saldo:
            return ('Saldo insuficiente.')
        elif valor > self.limite_saque:
            return ('Limite de saque excedido. Tente novamente.')
        elif self.limite_qtd_saque == 0:
            return ('Limite de saques atingido. Tente novamente em 24h.')
        else:
            self.saldo -= valor
            self.limite_qtd_saque -= 1
            self.historico += f'Saque de R$ {valor:.2f}\n'
            return ('Saque efetuado com sucesso.')

    def mostrar_extrato(self):
        extrato = "\n================ EXTRATO ================\n"
        if self.historico == '':
            extrato += 'Nenhum movimento realizado.'
        else:
            extrato += str(self.historico)
        extrato += f"\nSaldo: R$ {self.saldo:.2f}"
        extrato += "\n=========================================="
        extrato += "\n"
        return extrato