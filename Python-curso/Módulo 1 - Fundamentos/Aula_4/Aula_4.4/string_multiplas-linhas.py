nome = "Guilherme"

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
"""

print(mensagem)

#Mostra a mensagem até com os recuos do 
#jeito que está na linha de programação

mensagem2 = f'''
   Olá meu nome é {nome},
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.
'''

print(mensagem2)

print(
    """
    ============== MENU ==============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ==================================

            Obrigado por utilizar o sistema!
    """

)