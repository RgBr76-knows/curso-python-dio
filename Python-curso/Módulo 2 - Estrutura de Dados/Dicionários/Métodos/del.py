contatos = {

"guilherme@gmail.com": {"nome": 'Guilherme', "telefone": '3333-1112'},
"rodrigo@gmail.com": {"nome": 'Rodrigo', "telefone": '3333-1234'},
"geovana@gmail.com": {"nome": 'Geovana', "telefone": '3333-5678'},
"giselle@gmail.com": {"nome": 'Giselle', "telefone": '3333-4321'}

}

#remover telefone da Giselle
del contatos["giselle@gmail.com"]["telefone"] 
print(contatos)

#remover chave inteira 
del contatos["guilherme@gmail.com"]
print(contatos)

#Apagou foi tudo
del contatos
print(contatos)