#Exemplo: Se saldo for maior ou igual a 2000, posso fazer o saque

#Estrutura condicional só com IFs
import sys


saldo = 2000.0

if saldo >= 2000:
    print("Realizando saque!")

if saldo < 2000:
    print("Saldo insuficiente!")

#Estrutura condicional If/Else

saldo = 2000.0

if saldo >= 2000:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")

#Estrutura condicinal ElIf

opcao = int(input("Informe uma opção [1] Sacar \n [2] Extrato"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    # ...
elif opcao == 2:
    valor = print("Exibindo o extrato")
else:
    sys.exit("Opção Inválida")