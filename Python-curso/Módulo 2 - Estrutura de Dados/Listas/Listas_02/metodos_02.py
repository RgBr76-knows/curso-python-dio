linguagens = ["python", "js", "css", "p", "Java", "p"]
linguagens.remove("p")
print(linguagens)

linguagens.reverse()
print(linguagens)

linguagens.sort() #alfabeticamente
print(linguagens)

linguagens.sort(reverse = True) #ao contrário 
print(linguagens)

linguagens.sort(key=lambda x: len(x)) #do menor(menos 
#letras para o maior mais letras)
print(linguagens)

linguagens.sort( key = lambda x: len(x), reverse = True)
#mais letras ---> menos letras
print(linguagens)