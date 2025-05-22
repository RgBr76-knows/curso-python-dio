lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)

print(id(l2), id(lista)) # para mostrar que são dois
#objetos/instâncias diferentes

l2[0] = 2

print(lista)
print(l2)

linguagens = ["python", "js", "css"]
print(linguagens)
linguagens.extend({"java", "csharp"})

print(linguagens)

print(linguagens.index("java")) #4

linguagens.pop()

print(linguagens) # tirou o csharp

