contatos = {

"guilherme@gmail.com": {"nome": 'Guilherme', "telefone": '3333-1112'},
"rodrigo@gmail.com": {"nome": 'Rodrigo', "telefone": '3333-1234'},
"geovana@gmail.com": {"nome": 'Geovana', "telefone": '3333-5678'},
"giselle@gmail.com": {"nome": 'Giselle', "telefone": '3333-4321'}

}

#In verificar existência

resultado = "guilherme@gmail.com" in contatos 
print(resultado)

resultado = "idade" in contatos 
print(resultado)

resultado = "nome" in contatos["geovana@gmail.com"]
print(resultado)
resultado = "telefone" in contatos["geovana@gmail.com"]
print(resultado)