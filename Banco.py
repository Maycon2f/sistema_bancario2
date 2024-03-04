
def saque(valor):
    
    if valor > saldo:
        return print("Você não possui esse valor em conta para sacar!.")
    
    elif limite_diario == 0:
        return print("Você esgotou o seu limite diario para saque.")
    
    else:
        return True

def deposito(numero):
    if numero <= 0:
        return print("Digite um valor positivo para saque")
    else:
        return True


def cadastro(a):
    lista_temp = []
    endereco = {}
    nome = str(input("Nome: "))
    data_nascimento = str(input("Data de nascimento: "))
    cpf = str(input("Cpf: "))
    for i, numero in enumerate(usuarios_conta):
        if cpf in usuarios_conta[i][2]:
            return print("Cpf já cadastrado!")
            break
    rua = str(input("Rua: "))
    nro = str(input("Numero: "))
    bairro = str(input("Bairro: "))
    cidade = str(input("Cidade: "))
    sigla = str(input("Estado: "))
    lista_temp.append(nome)
    lista_temp.append(data_nascimento)
    lista_temp.append(cpf)
    endereco["rua"] = rua
    endereco["numero"] = nro
    endereco["bairro"] = bairro
    endereco["cidade"] = cidade
    endereco["sigla"] = sigla
    lista_temp.append(endereco)
    usuarios_conta.append(lista_temp)
    lista_temp.clear
    endereco.clear
    print("Usuario cadastrado com sucesso!")

saldo = 500
limite_diario = 3
extrato = [[],[]]
usuarios_conta = []
numero_contas = 0
lista_temporaria = []

while True:
    menu = int(input(' \nBoas Vindas ao banco PYTHON.\n Escolha uma opção:\n 1-|Saque \n 2-|Depósito \n 3-|Limite \n 4-|Extrato \n 5-|Cadastrar usuario \n 6-|Criar conta corrente \n 0-|Sair\n'))
    print
    if menu == 1:
        print(f"\nValor disponivel para saque R${saldo:.2f}\n")
        valor = int(input("qual o valor que você gostaria de sacar?: "))
        if saque(valor) == True:
            saldo -= valor
            limite_diario -= 1
            print(f"\nSaque de R${valor:.2f} realizado com sucesso!\n")
            extrato[0].append(valor)   
    elif menu == 2:
        valor = float(input("Qual o valor que voce gostaria de depositar?: "))
        if deposito(valor) == True:
            valor += saldo
            extrato[1].append(valor)
            print(f"Valor de R${valor:.2f} depositado com sucesso!.")
    elif menu == 3:
        print(f"Limite diario para saque {limite_diario}")
    elif menu == 4:
        print("Extrato".center(25, "="))

        print("Saque")
        for item in extrato[0]:
            
            print(f"R$".lstrip(), f"{item:.2f}".center(8, " "))
        print()
        print("Deposito")
        for item in extrato[1]:
            
            print(f"R$".lstrip(), f"{item:.2f}".center(8, " "))
        print("Extrato".center(25, "="))
    
    elif menu == 5:
        cadastro(True)
        print()
        print("usuarios cadastrados!")
        print()
        for i, usuario in enumerate(usuarios_conta):
            for item in usuarios_conta[i]:
                print(item)

    elif menu == 6:
        angecia = "0001"
        numero_contas += 1
        lista_temporaria.append(angecia)
        lista_temporaria.append(numero_contas)
        for i, usuario in enumerate(usuarios_conta):
            for item in usuarios_conta:
                usuarios_conta[i].append(lista_temporaria)
        lista_temporaria.clear

    elif menu == 0:
        print("Saindo...")
        break

    
    

        


    
    