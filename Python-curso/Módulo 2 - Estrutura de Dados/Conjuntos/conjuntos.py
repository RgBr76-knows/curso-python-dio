lista = [1, 4, 2, 8, 3, 4, 5]

#esse sorted é tipo um sort(), só que para usar no meio da instância
#Esse Set() é para tirar os repetidos 
print(sorted(set(lista)))

# Só assim para iterar e transformar em um set
numeros = {1, 2, 3, 4} #meu set
numeros = list(numeros) #converter para set
print(numeros[1])

# Não posso acessar o set sem transformar ele em uma lista