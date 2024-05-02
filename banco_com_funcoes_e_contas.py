

menu = """

[d] Realizar depósito
[s] Realizar saque
[e] Consultar Extrato
[cc] Cadastrar conta
[cu] Cadastrar usuário
[q] Sair

=> """

usuarios = []
contas = []

LIMITE_SAQUES = 3

def criar_usuario():
    print("Para criar o usuário, serão solicitados: nome, data de nascimento, CPF e endereço (formado por logradouro, número, bairro, cidade e estado.)")
    nome = input("Digite o nome do usuário: ")
    data = input("Digite a data de nascimento do usuário: ")
    cpf = input("Digite o CPF do usuário: ")

    for i in range(0,len(usuarios)):
        it = usuarios[i]
        if it['CPF'] == cpf:
            print("Erro: Já existe um usuário com este CPF.")
            return 
        
        #compara_cpf = usuarios[i].setdefault('CPF')
        #if compara_cpf == cpf:
        #    print("Erro: Já existe um usuário com este CPF.")
        #   return 
        
    logradouro = input("Digite o logradouro do usuário: ")
    numero = input("Digite o número do endereço usuário: ")
    bairro = input("Digite o bairro do usuário: ")
    cidade = input("Digite a cidade do usuário: ")
    estado = input("Digite a sigla do estado do usuário: ")
    endereco = logradouro + ", " + numero + " - " + bairro + " - " + cidade + "/" + estado
    usuarios.append({'Nome': nome, 'Data de nascimento': data, 'CPF': cpf, 'Endereço': endereco})
    print("Usuário adicionado com sucesso!")



def criar_conta():
        
    if len(usuarios)==0:
        print("Erro: Não há usuários cadastrados a quem possa ser atribuido uma conta.")
    else:
        cpf_usuario = input("Digite o CPF do titular da conta. ")

        for i in range(0,len(usuarios)):
            it = usuarios[i]
            if it['CPF'] == cpf_usuario:
                break
            print("Erro: Não há cadastrado usuário portador deste CPF.")
            
        
        if len(contas) == 0:
            numero = 1
        else:
            numero = (contas[-1])['Número'] + 1
        
        saldo = 0
        limite = 500
        extrato = ""
        numero_saques = 0

        for i in range(0,len(usuarios)):
            it = usuarios[i]
            if it['CPF'] == cpf_usuario:
                usuario = usuarios[i]
            
        contas.append({'Agência': '0001', 'Número': numero, 'Usuário': usuario, 'Saldo': saldo, 'Limite': limite, 'Extrato': extrato, 'Número de saques': numero_saques, 'Limite de saques': LIMITE_SAQUES})
        print("Conta adicionada com sucesso! O número da conta é ", numero)



def deposito(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor < 0:
        print("Impossível fazer deósito negativo.")
    else: 
        print("Depósito realizado com sucesso.")
        saldo = saldo + valor
        extrato = extrato + f"Depósito de {valor} reais. \n"

    return saldo, extrato



def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print("Saque")
    if numero_saques > 3:
        print("Erro: número de saques diário excedido.")
    else:
        saque = float(input("Digite o valor do saque: "))
        if saldo - valor < 0:
            print("Impossível realizar este saque: saldo insuficiente.")
        elif valor > LIMITE_SAQUES:
            print("Impossível realizar este saque: limite para saques excedido.")
        else: 
            numero_saques = numero_saques + 1
            print("Saque realizado com sucesso.")
            saldo = saldo - valor
            extrato = extrato + f"Saque de {valor} reais.\n"

    return saldo, extrato, numero_saques



def extrato(saldo,/,*,extrato):
    print("Extrato")
    print(f"Saldo atual da conta: R${saldo:.2f}.\nOperações anteriores:\n")
    print(f"{extrato}")



while True: 

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        existe_conta = 0
        num_conta = int(input("Informe o número da conta a qual será feito o depósito: "))
        for i in range(0,len(contas)):
            it = contas[i]
            if it['Número'] == num_conta:
                existe_conta = 1
                conta = contas[i]
            
        if existe_conta == 0:
            print("Erro: Não existe conta com o número fornecido.")
            break

        valor_deposito = float(input("Digite o valor do depósito: "))
        (conta['Saldo'], conta["Extrato"]) = deposito(saldo = conta['Saldo'], valor = valor_deposito, extrato = conta["Extrato"], limite = conta['Limite'], numero_saques = conta['Número de saques'], limite_saques = LIMITE_SAQUES)
        

    elif opcao == "s":    
        print("Saque")  
        existe_conta = 0
        num_conta = int(input("Informe o número da conta da qual será feito o saque: "))
        for i in range(0,len(contas)):
            it = contas[i]
            if it['Número'] == num_conta:
                existe_conta = 1
                conta = contas[i]
            
        if existe_conta == 0:
            print("Erro: Não existe conta com o número fornecido.")
            break

        valor_saque = float(input("Digite o valor do saque: "))
        (conta['Saldo'], conta["Extrato"], conta['Número de saques']) = saque(saldo = conta['Saldo'], valor = valor_saque, extrato = conta["Extrato"], limite = conta['Limite'], numero_saques = conta['Número de saques'], limite_saques = LIMITE_SAQUES)


    elif opcao == "e":
        print("Extrato")
        existe_conta = 0
        num_conta = int(input("Informe o número da conta: "))
        for i in range(0,len(contas)):
            it = contas[i]
            if it['Número'] == num_conta:
                existe_conta = 1
                conta = contas[i]
            
        if existe_conta == 0:
            print("Erro: Não existe conta com o número fornecido.")
            break

        extrato(conta['Saldo'], extrato = conta['Extrato'])

    elif opcao == "cc":
        criar_conta()



    elif opcao == "cu":
        criar_usuario()


    elif opcao == "q":
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")        
