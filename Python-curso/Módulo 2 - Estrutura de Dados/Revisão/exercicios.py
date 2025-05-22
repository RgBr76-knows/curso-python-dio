# Exercício 1
# Dada a lista de tuplas produtos = [("maçã", 2), ("banana", 3), ("cereja", 5)], percorra a lista e imprima o nome do produto apenas
# se a quantidade for maior que 2.

# # produtos = [("maçã", 2), ("banana", 3), ("cereja", 5)]

# # for produto, quantidade in produtos:
# #     if quantidade > 2:
# #         print(produto)



# Exercício 2
# Crie um dicionário chamado estoque onde as chaves são os nomes das frutas e os valores são as quantidades. 
# Verifique se todas as frutas no dicionário têm quantidades maiores que 5. 
# Caso contrário, imprima o nome da fruta com quantidade insuficiente.

# estoque = {

#     "banana" :      {"quantidade": 5 },
#     "uva"    :      {"quantidade": 8 },
#     "laranja":      {"quantidade": 3 },
#     "caqui"  :      {"quantidade": 10 },
#     "tomate" :      {"quantidade": 8 }
# }

# for frutas, quantidades in estoque.items():
#     quantidades = quantidades["quantidade"]
#     if quantidades < 5:
#         print(frutas + " esta com quantidade insuficiente")



# Exercício ESPECIAL 
# Crie uma variável para acessar a quantidade de cada fruta.
# Utilize um loop para iterar sobre o dicionário e verificar as quantidades.
# Atualize a quantidade de frutas insuficientes para 5 e registre o nome da fruta na lista atualizadas.
# Imprima a lista atualizadas com os nomes das frutas que foram atualizadas.

# estoque = {

#     "banana" :      {"quantidade": 5 },
#     "uva"    :      {"quantidade": 2 },
#     "laranja":      {"quantidade": 3 },
#     "caqui"  :      {"quantidade": 10 },
#     "tomate" :      {"quantidade": 1 }
# }

# atualizadas = []

# for frutas, quantidade in estoque.items():
#     quantidade = quantidade["quantidade"]
    
#     if quantidade <= 5:
#         quantidade = 5
#         atualizadas.append(frutas)


# for frutas in atualizadas:
#     print(frutas)


# Exercício 3
# Dado o conjunto pares = {2, 4, 6, 8, 10}, percorra o conjunto e imprima "Número Par" para cada elemento que estiver no conjunto 
# e "Número Ímpar" para os números de 1 a 10 que não estiverem no conjunto.

# pares = {2, 4, 6, 8, 10}
# for num in range (0,11):
#     if num  % 2 == 0:
#         print(str(num) + " e um numero par")
#     elif num % 2 != 0:
#         print(str(num) + " e um numero impar")



# Exercício 4
# Dada a tupla valores = (10, 20, 30, 40, 50), transforme a tupla em uma lista, multiplique cada 
# elemento por 2 e depois converta de volta para uma tupla.

# valores = (10, 20, 30, 40, 50)
# lista2 = []

# for num in valores:
#     num *= 2
#     lista2.append(num)

# print(lista2)   

# Exercicio 4 COPILOT
# Tupla original
# valores = (10, 20, 30, 40, 50)

# # Converter a tupla em uma lista
# lista_valores = list(valores)

# # Multiplicar cada elemento por 2
# for i in range(len(lista_valores)):
#     lista_valores[i] *= 2

# # Converter a lista de volta para uma tupla
# valores_modificados = tuple(lista_valores)

# # Imprimir a tupla resultante
# print(valores_modificados)



# Exercicio 5 

# Dado o dicionário pontos = {"João": 15, "Maria": 20, "Pedro": 12},
# crie um conjunto contendo apenas os nomes dos jogadores que têm mais de 14 pontos.

# # Dicionário original
# pontos = {"João": 15, "Maria": 20, "Pedro": 12}

# # Criação do conjunto com nomes dos jogadores que têm mais de 14 pontos
# jogadores = {nome for nome, pontos in pontos.items() if pontos > 14}

# # Imprimir o conjunto resultante
# print(jogadores)







    
        



            

