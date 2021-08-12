
# Crie um programa onde o usuário posso digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
pares = list()
impares = list()
lista[0] = pares
lista[1] = impares

for contador in range(1, 8):

    valores = int(input(f'Digite o {contador}º valor: '))

    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)

pares.sort()
impares.sort()

print('—' * 50)
print(f'Valores pares em ordem crescente → {lista[0]} ←')
print(f'Valores ímpares em ordem crescente → {lista[1]} ←')
print('—' * 50)