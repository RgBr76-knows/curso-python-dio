contatos = {

"guilherme@gmail.com": {"nome": 'Guilherme', "telefone": '3333-1112'},
"rodrigo@gmail.com": {"nome": 'Rodrigo', "telefone": '3333-1234'},
"geovana@gmail.com": {"nome": 'Geovana', "telefone": '3333-5678'},
"giselle@gmail.com": {"nome": 'Giselle', "telefone": '3333-4321'}

}
#Método copy
contatos_2 = contatos.copy()

print(contatos_2)

#Método clear
contatos_2.clear()
print(contatos_2)

#From keys

print(dict.fromkeys(["nome", "telefone"])) #colocar chaves sem ter nenhum valor
print(dict.fromkeys(["nome", "telefone"], "vazio")) #colocar chaves com o mesmo valor






