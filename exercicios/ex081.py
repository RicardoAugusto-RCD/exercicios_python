
# Crie um programa que vai ler vários números em uma lista.
# Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('—' * 50)
print(f'Foram digitados → {len(lista)} ← números')
print('—' * 50)

listaOrdenada = sorted(lista, reverse=True)
print(f'Lista ordenada de forma decrescente → {listaOrdenada} ←')

print('—' * 50)
if 5 in lista:
    print(f'O número 5 apareceu primeiramente na → {listaOrdenada.index(5) + 1}ª ← Posição')
else:
    print('O número 5 não foi digitado')
print('—' * 50)
