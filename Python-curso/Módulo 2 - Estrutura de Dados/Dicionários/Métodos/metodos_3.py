contatos = {

 "nome": 'Guilherme', "telefone": '3333-1112'
}

#SET DEFAULT - adicionar caso objeto não exista

contatos.setdefault("nome", "Giovanna")
print(contatos) #não vai criar o nome : Giovanna pq já
#existe um objeto nome

contatos.setdefault("idade", 28)
print(contatos) #Cria pq n tinha nenhum objeto chamado idade


#POP ITEM - retira itens na sequência, dá erro qnd n tem 
#mais bosta nenhuma

print(contatos.popitem())
print(contatos.popitem())
print(contatos.popitem())
print(contatos.popitem())





