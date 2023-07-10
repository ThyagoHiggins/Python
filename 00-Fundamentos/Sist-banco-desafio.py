from datetime import datetime
import time

depositos = dict()
historico_depo = list()

saques = dict()
historico_saque = list()
qtdsaques = 0

saldo = 1500
data = datetime.now()
date = data.strftime("%d/%m/%Y ")
hour = data.strftime("%H:%M")

op = ""
dep = ""

while op != 0:
    print("*" * 10)
    print("Bem-vindo ao DIOBANK ")
    print(date, hour)
    print("*" * 10)

    print(f"Seu saldo é de R$ {saldo}")
    print("*" * 10)
    print("Escolha uma opção abaixo:")
    print("[1] Depósito")
    print("[2]Saque")
    print("[3]Extrato")
    print("[0] Sair")
    print("*" * 10)
    op = int(input("Digite a opção:"))
    print(op)

    if op == 1:
        print("#" * 10)
        print("Você está depositando... ")
        print("#" * 10)
        dep = 0
        while dep <= 0:
            dep = float(input("Digite o valor de Depósito: R$ ").replace(",", "."))

            print("")

            print(f"Valor a ser depositado é R$ {dep:.2f}")

            conf = input("Você confirma? [Y/N]: ")

            if conf.upper() == "Y":
                print("depositado ")
                saldo += dep
                depositos["Data: "] = date
                depositos["Hora: "] = hour
                depositos["Valor: R$"] = dep

                historico_depo.append(depositos)

            if dep <= 0:
                print("Informe valor maior que 0!")

    elif op == 2:
        print("#" * 10)
        print("Você está Sacando... ")
        print("#" * 10)
        sac = 0
        while sac <= 0:
            sac = float(input("Digite o valor de Saque: R$ ").replace(",", "."))

            print("")

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

       
    elif op == 3:
       
            print("=" * 10, "EXTRATO", "=" * 10)

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
                print()

            print("_" * 10)
            print(f"Seu saldo é de R$ {saldo:.2f}")
            print("_" * 10)

    elif op == 0:
        print("saindo do sistema")
        time.sleep(2)
        print("Você saiu!")
