conta_normal = ...
conta_universitaria = ...

conta = int(input("Qual conta será usada: \n" + "[1] - Normal \n [2] - universitária: "))
if conta == 1:
    conta_normal = True 
    saldo = float(input("Qual o seu saldo atual: "))
    cheque_especial = float(input("Qual é o valor do seu cheque especial atual: "))
    saque = float(input("Qual é o valor do seu saque: "))

elif conta == 2:
    conta_universitaria = True 
    saldo = float(input("Qual o seu saldo atual: "))
    saque = float(input("Qual é o valor do seu saque: "))
else:
    print("Conta inválida")





if conta_normal == True: 
    if saldo >= saque:

        print("Saque realizado com sucesso")

    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial")
    
    elif saque > (saldo + cheque_especial):
        print("Saldo insuficiente!")

elif conta_universitaria == True:
    if saldo > saque:

        print("Saque realizado com sucesso!")

    else:
        print("Saldo insuficiente!")