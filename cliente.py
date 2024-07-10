class Cliente:
    def __init__(self, nome, dtnasc, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.dtnasc = dtnasc
        self.endereco = endereco
        self.contas = [] # lista de contas

    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nData de nascimento: {self.dtnasc}\nEndereço: {self.endereco}\nLista de contas: {self.contas}\nConta: {self.conta}s'
    
    def inserir_conta(self, conta):
        self.contas.append(conta)
    
