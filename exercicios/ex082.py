
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# No final mostre o conteúdo das três listas geradas.

listaA = []
listaB = []
listaC = []

print('—' * 80)
while True:

    numero = int(input('Digite um número: '))
    listaA.append(numero)

    if numero % 2 == 0:
        listaB.append(numero)
    else:
        listaC.append(numero)

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('—' * 80)
    if resposta == 'N':
        break

print('—' * 80)
print(f'Conteúdo da lista com todos os números → {listaA} ←')

print('—' * 80)
print(f'Conteúdo da lista com apenas números pares → {listaB} ←')

print('—' * 80)
print(f'Conteúdo da lista com apenas números impares → {listaC} ←')
print('—' * 80)