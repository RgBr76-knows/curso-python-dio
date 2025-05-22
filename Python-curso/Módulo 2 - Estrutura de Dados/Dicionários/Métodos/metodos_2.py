contatos = {

"guilherme@gmail.com": {"nome": 'Guilherme', "telefone": '3333-1112'}
}

#print(contatos["chave"]) #Key error pq a chave n existe

##GET
print(contatos.get("chave"))
print(contatos.get("chave", {})) #se o get não encontrar a chave
#ele retorna um dicionário vazio
print(contatos.get("guilherme@gmail.com", {}))
#Se ele encontra, retorna o dicionário 

##ITENS
print(contatos.items())
#retorna um conjunto de tuplas

##KEYS

print(contatos.keys())
#Retorna as chaves (exemplo chave --> Nome : Rodrigo)

#Exclui a chave 
resultado = contatos.pop("guilherme@gmail.com")
print(resultado)

#Não sei se exclui, para ter certeza o pop deixa 
#colocar uma mensagem tipo o Alt e IMG do HTMl
resultado = contatos.pop("guilherme@gmail.com", "Objeto ja removido burro")
print(resultado)

