
# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais.
# Isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes.

reta1 = float(input('Digite o valor da reta 1: '))

reta2 = float(input('Digite o valor da reta 2: '))

reta3 = float(input('Digite o valor da reta 3: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Formam um triângulo? SIM')

    if reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('Escaleno')

    elif reta1 == reta2 and reta2 == reta3 and reta3 == reta1:
        print('Equilátero')

    else:
        print('Isósceles')

else:
    print('Formam um triângulo? NÃO')
