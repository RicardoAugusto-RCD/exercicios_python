
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print('—' * 60)

lista = []

for contador in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {contador}: ')))

maior = max(lista)
menor = min(lista)

print('—' * 60)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi → {maior} ← e apareceu na Posição → {lista.index(maior)} ←')
print(f'O menor valor digitado foi → {menor} ← e apareceu na Posição → {lista.index(menor)} ←')
print('—' * 60)
