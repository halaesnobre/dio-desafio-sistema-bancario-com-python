from cliente import Cliente
from conta import Conta

clientes = []

if __name__ == '__main__':
    menu = """Menu de operações:\n
    1 - Operações de cadastro\n
    2 - Operações de conta\n
    0 - Sair\n"""
    sub_menu_cadastro = """
    1 - Cadastrar novo cliente\n
    2 - Cadastrar conta\n
    0 - retornar\n"""
    sub_menu_conta = """
    1 - Depositar\n
    2 - Sacar\n
    3 - Extrato\n
    0 - retornar\n
    """
    while True:
        print(menu)
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            cadastro = True
            while cadastro == True:
                print(sub_menu_cadastro)
                opcao_cadastro = int(input('Escolha uma opção: '))
                if opcao_cadastro == 1:
                    nome = input('Informe o Nome completo: ')
                    dtnasc = input('Data de nascimento: *dd-mm-aaaa* ')
                    cpf = input('CPF: *somente numeros* ')
                    endereco = input('Endereço: *Logradouro, nro - bairro - cidade/UF* ')
                    cliente = Cliente(nome, dtnasc, cpf, endereco)
                    clientes.append(cliente)
                if opcao_cadastro == 2:
                    cpf = input('Informe o CPF do cliente: *somente numeros* ')
                    cliente = next((c for c in clientes if c.cpf == cpf), None)
                    if not cliente:
                        print('Cliente não encontrado')
                        continue
                    else:
                        conta = input('Conta: ')
                        cliente.inserir_conta(Conta(agencia="0001", conta=conta, saldo=0))
                        print('Conta criada com sucesso!')
                if opcao_cadastro == 0:
                    cadastro = False
        if opcao == 2:
            cpf = input('Informe o CPF do cliente: *somente numeros* ')
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if not cliente:
                print('Cliente não encontrado')
                continue
            else:
                conta = input('Informe a Conta: ')
                conta = next((c for c in cliente.contas if c.conta == conta), None)
                if not conta:
                    print('Conta não encontrada')
                    continue
                else:                
                    operacoes = True
                    while operacoes == True:
                        print(sub_menu_conta)
                        opcao_operacao = int(input('Escolha uma opção: '))
                        if opcao_operacao == 1:
                            valor = float(input('Qual valor deseja depositar? '))
                            print(conta.depositar(valor))
                        if opcao_operacao == 2:
                            valor = float(input('Qual valor deseja sacar? '))
                            print(conta.sacar(valor))
                        if opcao_operacao == 3:
                            print(conta.mostrar_extrato())
                        if opcao_operacao == 0:
                            break
                if opcao_operacao == 0:
                    operacoes = False

        if opcao == 0:
            break