
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = menor = 0

print('—' * 60)
for contador in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {contador}: ')))

    if contador == 0:
        maior = menor = lista[contador]
    else:
        if lista[contador] > maior:
            maior = lista[contador]
        if lista[contador] < menor:
            menor = lista[contador]

print('—' * 60)
print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()
print('—' * 60)


