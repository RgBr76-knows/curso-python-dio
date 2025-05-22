

##### LISTAS #####


# ESPECIAL
# Exercício : Adicionar Elementos
# Crie uma lista vazia chamada nomes.

# Peça ao usuário para inserir 5 nomes e adicione-os à lista utilizando um loop for.

# Imprima a lista resultante.

# lista = []
# for i in range(0,5):
#     nome = input("Entre com um nome: ")
#     lista.append(nome)

# print(lista)





#ESPECIAL
# Exercício 3: Média de Notas
# Crie uma lista com 5 notas de alunos.

# Utilize um loop for para calcular a média das notas.

# Utilize a estrutura if para verificar se a média é maior ou igual a 6. Se for, imprima "Aprovado", 
# caso contrário, imprima "Reprovado".

# lista_nota_final = []
# nomes= []

# alunos = input("Entre com a quantidade de alunos: ")
# qntd_notas = input("Entre com a quantidade de notas: ")

# for i in range(0, int(alunos)):
#     nomes.append(input("Entre com o nome do aluno: "))


# for i in range(0, int(alunos)):
#     print(nomes[i])
#     ac = 0
#     for i2 in range(0, int(qntd_notas)):
#         nota = int(input(f"Entre com sua {i2+1} ª nota: "))
#         ac += nota
#     md = ac / int(qntd_notas)
#     lista_nota_final.append(int(md))


# for i in range(0, int(alunos)):
#     if lista_nota_final[i] >= 6:
#         print("A media do(a) aluno(a) " + str(nomes[i]) + " ---> " + str(lista_nota_final[i]))
#         print("Situacao - Aprovado!")
#     else:
#         print("A media do(a) aluno(a) " + str(nomes[i]) + " ---> " + str(lista_nota_final[i]))
#         print("Situacao - Reprovado!")





# ESPECIAL
# Exercício 4: Copiar e Limpar Lista
# Crie uma lista com 3 frutas: ["maçã", "banana", "cereja"].

# Faça uma cópia da lista utilizando o método copy.

# Limpe a lista original utilizando o método clear.

# Imprima as duas listas para verificar os resultados.

# lista = []
# qntd_frutas = int(input("Entre com a quantidade de frutas: "))

# for i in range(0, qntd_frutas):
#     fruta = input("Qual fruta deseja adicionar? : ")
#     lista.append(fruta)

# frutas = lista.copy()
# lista.clear()

# print(frutas, lista)



# ESPECIAL
# Exercício 5: Multiplicar Elementos
# Crie uma lista com os números de 1 a 5.

# Utilize um loop for para multiplicar cada elemento da lista por 2.

# Imprima a lista resultante.

# lista = [1, 2, 3, 4, 5]
# lista_atualizada =[]

# for i in range(0, len(lista)):
#     mult = lista[i] * 2
#     lista_atualizada.append(mult)


# print(lista_atualizada)




# ESPECIAL
# Exercício 6: Números de 1 a 20
# Utilize a função range para criar uma lista com os números de 1 a 20.

# Percorra a lista utilizando um loop for e imprima cada número.

# lista = []

# for i in range(1, 21):
#     lista.append(i)

# print(lista)




# Exercício 7: Soma de Elementos
# Crie uma lista com 5 números.

# Utilize um loop for para calcular a soma dos elementos da lista.

# Imprima a soma resultante.
# import random

# lista = []
# ac = 0
# for i in range (0 , 5):
#     num = random.randint(1, 10)
#     lista.append(num)

#     ac += num

# print("Lista: " + str(lista))
# print("Soma resultante dos numeros da lista : " + str(ac))





# ESPECIAL
# Exercício 8: Verificar Presença de Elemento
# Crie uma lista com alguns elementos (por exemplo, ["maçã", "banana", "cereja"]).

# Peça ao usuário para inserir um elemento.

# Utilize a estrutura if para verificar se o elemento inserido está na lista e imprima uma mensagem apropriada.

# lista = []
# qntd_frutas = int(input("Quantas frutas colocara na lista? --> "))

# for i2 in range(0, qntd_frutas):
#     frutas = str(input(f"Nome da {i2+1}ª fruta:  "))
#     lista.append(frutas.title())


# elemento = str(input("Entre com uma fruta: ")).title()

# if elemento in lista:
#     print(f"Elemento: {elemento} esta na lista \n Lista: {lista}")
# else:
#     print(f"Elemento: {elemento} nao esta na lista \n Lista: {lista}")


    

#ESPECIAl
# Exercício 9: Concatenar Listas
# Crie duas listas: lista1 com os números de 1 a 3 e lista2 com os números de 4 a 6.

# Utilize o operador + para concatenar as duas listas em uma nova lista chamada lista3.

# Imprima a lista resultante.

# #Lista que o exercício pede

# lista = [1,2,3] 
# lista2 = [4,5,6]

# lista3 = lista + lista2

# print(lista3)

# #Copilot, vê se esse uso de ramdom foi correto e está bom

# import random

# lista =[]
# lista2 = []

# for i in range(0,3):
#     num = random.randint(1,10)
#     lista.append(num)

# for i in range(0,3):
#     num = random.randint(1,10)
#     lista2.append(num)

# lista3 = lista + lista2
# print(lista3)




##### TUPLAS #####



#ESPECIAL
# Escreva um programa que receba uma tupla de números e retorne uma lista apenas com os números positivos. 
# Utilize um loop for e a estrutura if para filtrar os números.
# Dica: Converta a tupla em uma lista antes de começar a adicionar os números positivos.

# Tupla = ()
# Lista = list(Tupla)

# qntd_loop = int(input("Entre com quantos numeros colocara na lista: "))

# if qntd_loop > 0:
#     for i in range(qntd_loop):
#         num = int(input("Entre com um numero positivo --> "))
#         if num > 0:
#             Lista.append(num)
#         else:
#             print("Seu filho da puta isso não e positivo!!!!!!")
#             break
# else:
#     print("Sorry, nao da para fazer essa estrutura de repeticao")

# Tupla = tuple(Lista)
# print(Tupla)




# ESPECIAL
# Crie um programa que receba uma lista de palavras e verifique se uma palavra específica está presente 
# nessa lista. Se a palavra estiver presente, imprima “Palavra encontrada!”; caso contrário, 
# imprima “Palavra não encontrada”. Utilize if e else.
# Dica: Você pode usar o operador in para verificar a presença da palavra na lista.


#Usando For

# import itertools

# for i in itertools.count(): 
#     lista_palavras = []
#     qntd_palavras = int(input("Quantas palavras deseja colocar: "))

#     # For para colocar as palavras dentro da lista
#     for i2 in range(0, qntd_palavras):
#         palavra = str(input("Qual palavra deseja escrever: "))
#         lista_palavras.append(palavra.lower())

#     qnt_words_to_compare = int(input("Entre com quantas palavras deseja conferir "
#     "se pertence a lista previamente criada: "))

#     for i3 in range(0, qnt_words_to_compare):
#         word_confere = str(input("Qual palavra deseja verificar ? --> "))
#         if word_confere.lower() in lista_palavras:
#             print("Palavra encontrada!!")
#         else:
#             print("Palavra não encontrada!!")


#     opcao = int(input("Deseja continuar ? \n"
#                   "[1] - SIM \n"
#                   "[2] - NAO \n"
#                   "Quaisquer outro numero colocado o programa fechara! \n"
#                   ">>> "))
#     if opcao == 1:
#         print("O programa continuara!")
#     else:
#         print("O programa encerrara!")
#         break





# ESPECIAL
# Escreva um programa que itere sobre uma lista de nomes e adicione todos os nomes que começam com a letra "A"
#  a uma nova lista. Utilize um loop for e a estrutura if.
# Dica: Utilize o método append() para adicionar os nomes à nova lista.


# lista_nomes = []
# comeca_A = []
# qnt_nomes = int(input("Quantos nomes deseja colocar na lista? \n >>> "))

# for i in range (0, qnt_nomes):
#     nome = str(input(f"Coloque o {i+1}º nome \n >>> "))
#     lista_nomes.append(nome.title())
#     if nome.lower().startswith("a"):
#         comeca_A.append(nome.title())
#     else:
#         continue

# print("Lista de nomes adicionados: \n" + str(lista_nomes))
# print("Nomes que começam com a letra A: \n" + str(comeca_A))




# ESPECIAL
# Desenvolva um programa que receba uma lista de números e calcule a 
# soma de todos os números ímpares. Utilize um loop for e a estrutura if.
# Dica: Verifique se o número é ímpar utilizando o operador %.

# lista_num = []
# lista_impar=[]
# qntd_num = int(input("Quantos numeros deseja digitar? \n>>> "))
# ac_impar = 0
# for i in range(qntd_num):
#     num = int(input(f"Coloque o {i+1}º numero \n>>> "))
#     lista_num.append(num)

# for i in range(len(lista_num)):
#     if lista_num[i] % 2 != 0:
#         ac_impar += lista_num[i]
#         lista_impar.append(lista_num[i])
    
# print("Lista \n>>> " + str(lista_num))
# print("Impares \n>>> " + str(lista_impar))
# print("Soma dos numeros impares \n>>> " + str(ac_impar))



# Crie um programa que peça ao usuário para inserir elementos em uma lista até que o usuário digite “sair”.
#  Utilize um loop while, if, e o método append().
# Dica: Verifique a condição de parada dentro do loop.

# import itertools

# lista = []
# print("Coloque qualquer elemento dentro da lista.\n"
#       "Caso deseje parar, digite [SAIR]")
# for i in itertools.count():
#     elemento = str(input(f"Coloque o {i+1}º elemento da lista\n>>> "))
#     if elemento.lower() == "sair":
#         break
#     else:
#         lista.append(elemento)

# print("Lista: " + str(lista))


#MEU CÓDIGO
 
    # Elabore um programa que receba uma tupla de palavras e transforme todas as palavras em maiúsculas, 
    # retornando uma nova lista com essas palavras. Utilize um loop for e o método upper().
    # Dica: Você pode usar uma list comprehension para tornar o código mais compacto.

    # palavras = [] #List para receber as palavras
    # qntd = int(input("Quantas palavras adicionará à sua lista\n >>> "))

    # for i in range(qntd):
    #     word = str(input(f"Digite sua {i + 1}ª palavra \n>>> "))
    #     palavras.append(word.upper())

    # Tupla = tuple(palavras)
    # print( "Sua tupla em letras MAIÚSCULAS está finalizada, veja o resultado! \n"
    #     "Tupla: " + str(Tupla))

#COPILOT ENSINANDO O LIST COMPREHENSION

    # # Solicita a quantidade de palavras
    # qntd = int(input("Quantas palavras adicionará à sua lista\n >>> "))

    # # Utiliza list comprehension para coletar as palavras e transformá-las em maiúsculas
    # palavras = [input(f"Digite sua {i + 1}ª palavra \n>>> ").upper() for i in range(qntd)]

    # # Converte a lista de palavras em uma tupla
    # Tupla = tuple(palavras)

    # print("Sua tupla em letras MAIÚSCULAS está finalizada, veja o resultado! \n"
    #     "Tupla: " + str(Tupla))






