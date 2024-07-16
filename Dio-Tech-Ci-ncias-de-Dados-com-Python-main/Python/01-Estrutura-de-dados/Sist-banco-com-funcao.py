from datetime import datetime
import time

# buscar as datas e hora no momento da movimentação

data = datetime.now()
date = data.strftime("%d/%m/%Y ")
hour = data.strftime("%H:%M")

#Organizar e alocar os históricos de depositos e saques para serem chamados depois nas opções do menu

depositos = dict()
historico_depo = list()
saques = dict()
historico_saque = list()

#Receber dados das movimentações
saldo= 600
qtdsaques = 0
user = list()
contas = list()


def menu():

    print("*" * 10)
    print("Bem-vindo ao DIOBANK ")
    print(date, hour)
    print("*" * 10)
    print(f"Seu saldo é de R$ {saldo:.2f}")
    print("Escolha uma opção abaixo:")
    print("[1] Depósito")
    print("[2] Saque")
    print("[3] Extrato")
    print("[4] Listar Contas")
    print("[5] Nova Conta")
    print("[6] Novo usuário")
    print("[0] Sair")
    print("*" * 10)
    opcao = int(input("Digite a opção:"))

    return opcao

def deposito(dep,depositos,historico_depo,/):
     global saldo
     print("")

     print(f"Valor a ser depositado é R$ {dep:.2f}")

     conf = input("Você confirma? [Y/N]: ")
     
     if dep <= 0: 
        print("Você tem que depositar um valor maior que 0")
     else:   
        if conf.upper() == "Y":
            print("depositado ")
            saldo += dep
            depositos["Data: "] = date
            depositos["Hora: "] = hour
            depositos["Valor: R$"] = dep
            historico_depo.append(depositos)
        else: 
            print('Voltando ao início...')
            
def saque(sac,saques, historico_saque):
    global saldo
    global qtdsaques
    
    if sac <= 0:
        print("Informe valor maior que 0!")
    elif saldo < sac:
        print("Você não tem Saldo")
    elif  qtdsaques > 3:
        print("Você atingiu o limite de saques")
    elif sac > 500:
        print("Você não pode sacar mais que R$ 500,00")

    else:
        print(f"Valor a ser Sacado é R$ {sac:.2f}")

        conf = input("Você confirma? [Y/N]: ")

        if conf.upper() == "Y":
            print("Saque realizado, retire seu dinheiro ")
            saldo -= sac
            qtdsaques += 1
            saques["Data: "] = date
            saques["Hora: "] = hour
            saques["Valor: R$"] = sac

            historico_saque.append(saques)

def extrato():

    global historico_depo, historico_saque
    
    print("=" * 10, "EXTRATO", "=" * 10)

    if not historico_depo or  not historico_saque:
        print("Sem movimentação")
    else:
        print("+" * 10, "Histórico de Depósitos", "+" * 10)
        for d in historico_depo:
            for x, y in d.items():
                print(f"{x}{y}", end=" ")
        print()
        print()

        print("+" * 10, "Histórico de Saques", "+" * 10)
        for s in historico_saque:
            for x, y in s.items():
                print(f"{x}{y}", end=" ")
        print()
        
    print("_" * 10)
    print(f"Seu saldo é de R$ {saldo:.2f}")
    print("_" * 10)
def usuario_novo(user):
    cpf = input("Insira seu CPF [somente números]: ")
    new_user = verficacpf(cpf)

    if new_user:
        print("Usuário já cadastrado")
    else:
        print("#" * 10)
        print("Realizando Cadastro... ")
        print("#" * 10)

        nome = input("Informe o nome: ")
        nasc = input ("Informe data de nascimento: ")
        end = input("Informe o endereço: ")
        user.append({"cpf": cpf,
                    "nome":nome,
                    "Data de Nascimento":nasc,
                    "Endereço":end})

        print('USUÁRIO CRIADO \O/')

def verficacpf(cpf, user):
    verifcado = [users for users in user if users["cpf"]== cpf]
    return verifcado[0] if verficado else None

def nova_conta(agencia,user,number):
    cpf = input("Insira seu CPF [somente números]: ")
    novaconta = verficacpf(cpf,users)

    if nova_conta:
        print ("A conta foi criada")
        return {"agencia": agencia,"conta-corrente":number, "user":novaconta}


def todas_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)

        print(linha)

def inicio():
    agencia = "0001"
    
    while True:
        op = menu()

        if op == 1:
        
            print("#" * 10)
            print("Você está depositando... ")
            print("#" * 10)
            
            dep = float(input("Digite o valor de Depósito: R$ ").replace(",", "."))
           
            saldo = deposito(dep,depositos,historico_depo)
            print(depositos)
        
        elif op == 2:
            print("#" * 10)
            print("Você está Sacando... ")
            print("#" * 10)
            
            sac = float(input("Digite o valor de Saque: R$ ").replace(",", "."))
            
            saque(sac,saques, historico_saque)

            print(saques)

        elif op == 3:
            extrato()
        elif op == 4:
            todas_contas(contas)
        elif op == 5:
            number = len(contas)+1
            new = nova_conta (agencia,user,number)

            if new:
                contas.append(new)
        elif op == 6:
            usuario_novo(user)
        elif op == 0:
            print("Saindo do Sistema...")
            print()
            print()

            time.sleep(2)
            print ( "Programa encerrado")
            break
        else:
            print("Selecione uma opção válida!!!!")
            
inicio()
