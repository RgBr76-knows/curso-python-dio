# Maiúsculo, minúsculo e título

curso = "Python" 
print(curso.upper())
# >>> PYTHON 

print(curso.lower())
# >>> python 

print(curso.title())
# >>> Python 

# Eliminando espaços

curso = "     Python  " 

##Esse + foi colocado para enxergar os espaços
print(curso.strip() + "+")
# >>> "Python"

print(curso.lstrip() + "+")
# >>> "Python  "

print(curso.rstrip() + "+")
# >>> "     Python"

# Junções e centralizações

curso = "Python" 

print(curso.center(10, "#"))
# >>> "##Python##"

print(".".join(curso))
# >>>"P.y.t.h.o.n"