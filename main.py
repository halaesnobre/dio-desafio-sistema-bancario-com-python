class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia 
        self.conta = conta
        self.saldo = saldo
        self.historico = ''
        self.limite_saque = 500
        self.limite_qtd_saque = 3
    
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


if __name__ == '__main__':
    menu = 'Menu de operações:\n1 - Depositar\n2 - Sacar\n3 - Extrato\n4 - Sair\n'
    conta = Conta(agencia=123, conta=123456, saldo=0)
    while True:
        print(menu)
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            valor = float(input('Qual valor deseja depositar? '))
            print(conta.depositar(valor))
        if opcao == 2:
            valor = float(input('Qual valor deseja sacar? '))
            print(conta.sacar(valor))
        if opcao == 3:
            print(conta.mostrar_extrato())
        if opcao == 4:
            break
