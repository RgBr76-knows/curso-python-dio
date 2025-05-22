# # for
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = "")

print() # quebra de linha



# ##For com range

print(range(4))

for numero in range (0, 11):
    print(numero, end = "")
# >>> 0 1 2 3 4 5 6 7 8 9 10

print("\n\n")



for numero in range(0, 51, 5):
    print(numero, end = "")
# Vai de 5 em 5 

print("\n\n")

###While

opcao = -1
while opcao != 0:
    opcao = int(input("[1]Sacar \n [2]Extrato \n [0]Sair"))
    if opcao == 1:
        print("Saque sendo realizado")
    elif opcao == 2:
        print("Extrato sendo realizado")
    else:
        opcao = 0 # Para caso coloquem um 3, ele feche o programa

print("\n\n")

# Break


while True: ## Laço infinito, só pode ser quebrado pelo Break
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)


for numero in range(100):
    if numero == 10:
        break # para por aqui

    print(numero, end=" ")

for numero in range(100):
    if numero == 10:
        continue # exibe todos os números menos o escolhido acima

    print(numero, end=" ")

while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10:
        break
    
    if numero % 2 == 0:
        continue

    print(numero)
#break antes, e o continue depois
