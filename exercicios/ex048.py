
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 a 500.

soma = 0
cont = 0

for c in range(3, 501, 6):

    soma = soma + c
    cont = cont + 1

print('A soma de todos os {} valores, entre 1 e 500 é {}'.format(cont, soma))


