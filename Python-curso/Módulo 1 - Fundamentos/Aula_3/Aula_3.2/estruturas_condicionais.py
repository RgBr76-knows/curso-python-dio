MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

#ifs
idade = int(input("Informe sua idade: "))
if idade >= MAIOR_IDADE:
    print("Pode tirar CNH! ")
if idade < MAIOR_IDADE:
    print("Não pode tirar a CNH! ")

#if/else
if idade >= MAIOR_IDADE:
    print("Pode tirar CNH! ")
else:
    print("Não pode tirar a CNH! ")

#ELIF - mesma coisa que ELSEIF na linguagem Java

if idade >= MAIOR_IDADE:
    print("Pode tirar CNH! ")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer as práticas ")
else:
    print("Não pode tirar a CNH! ")


