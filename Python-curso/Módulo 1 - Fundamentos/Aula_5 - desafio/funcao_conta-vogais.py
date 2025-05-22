def conta_vogais(texto):
    # Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    VOGAIS = "aeiouAEIOU"
    

    # Inicialize um contador para contar as vogais:
    contador = 0
    
    # esse char, é a variável que conta qnts caractéres tem no texto para fazer a estrutura de repetição
    # Iteramos pelos caracteres da string
    for char in texto: 
        # Verifique se o caractere atual é uma vogal e incremente o valor do contador:
        if char in VOGAIS:
            contador += 1
    
    return contador

# Solicitamos ao usuário que insira uma string
texto = input("Entre com um texto :")


# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")