#set também faz união

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b)) #Union(), união dos
#conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {3, 2, 5}

print(conjunto_a.intersection(conjunto_b)) 
#Intersection - intersecção 

conjunto_a = {1, 2, 3}
conjunto_b = {3, 2, 5}

print(conjunto_a.difference(conjunto_b)) 
print(conjunto_b.difference(conjunto_a)) 
#Difference - tira a diferença de tudo que tem no 
#conjunto A e no conjunto B, ou vice-versa

conjunto_a = {1, 2, 3}
conjunto_b = {3, 2, 5}

print(conjunto_a.symmetric_difference(conjunto_b)) 
#Symmetric_difference é a diferença que tem em ambos

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 4, 6, 3}

#Todos os elementos de A estão em B?
print(conjunto_a.issubset(conjunto_b))

#Todos os elementos de B estão em A?
print(conjunto_b.issubset(conjunto_a))

#Ao contrário - issuperset

print(conjunto_a.issuperset(conjunto_b))

#isdisjoint conjunto que não se toca

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b)) # A não está em B - TRUE
print(conjunto_a.isdisjoint(conjunto_c)) # A tem elementos em C - FALSE

sorteio = {1, 23}

sorteio.add(25)
#add adiciona

sorteio_2 = sorteio.copy() #copy copia o sorteio

sorteio.clear()
print(sorteio)
print(sorteio_2) # clear limpa o sorteio

numeros = {1, 2, 2, 3 ,4,  4, 5, 6,7,  7, 8, 9}

numeros.discard(1) # descartamos o 1
print(numeros)
numeros.discard(45) # n tem 45 então foda-se, descartou merda nenhuma
print(numeros)

numeros.pop() # tira da esquerda pra direita
print(numeros)

#remove parecido com o discard, mas se eu colocar no remove
#um elemento que não exite, DÁ ERRO.
#Diferença entre o remove e o discard peste acéfala

print(len(numeros)) # conta quantos objetos temos dentro da variável set()

print(1 in numeros ) # False 1 não está em números
