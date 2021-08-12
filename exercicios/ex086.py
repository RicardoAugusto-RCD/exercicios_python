
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

lista1 = [[], [], []]
lista2 = [[], [], []]
lista3 = [[], [], []]

for linha in range(1, 4):

    for coluna in range(0, 3):
        valores = int(input('Digite um v: '))

        if linha == 1:
            lista1[coluna] = valores
        if linha == 2:
            lista2[coluna] = valores
        if linha == 3:
            lista3[coluna] = valores

print('—' * 15)
print([lista1[0]], [lista1[1]], [lista1[2]])
print([lista2[0]], [lista2[1]], [lista2[2]])
print([lista3[0]], [lista3[1]], [lista3[2]])
print('—' * 15)



