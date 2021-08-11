
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção(sem usar o sort()).
# No final mostre a lista ordenada na tela.

lista = []

for contador in range(1, 6):

    valor = int(input(f'Digite um valor: '))

    if contador == 1:
        lista.append(valor)
        print(f'Foi adicionada a {contador}ª Posição')

    if contador == 2:
        if valor >= lista[0]:
            lista.append(valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')
        else:
            lista.insert(0, valor)
            print(f'Foi adicionado a {lista.index(valor) + 1}ª Posição')

    if contador == 3:
        if valor >= lista[0] and valor >= lista[1]:
            lista.append(valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')
        elif valor >= lista[0]:
            lista.insert(1, valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')
        else:
            lista.insert(0, valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')

    if contador == 4:
        if valor >= lista[2]:
            lista.append(valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')
        elif valor >= lista[1]:
            lista.insert(2, valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')
        elif valor >= lista[0]:
            lista.insert(1, valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')
        else:
            lista.insert(0, valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')

    if contador == 5:
        if valor >= lista[3]:
            lista.append(valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')
        elif valor >= lista[2]:
            lista.insert(3, valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')
        elif valor >= lista[1]:
            lista.insert(2, valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')
        elif valor >= lista[0]:
            lista.insert(1, valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')
        else:
            lista.insert(0, valor)
            print(f'Foi adicionado na {lista.index(valor) + 1}ª Posição')

print('—' * 50)
print(f'Lista ordenada → {lista} ←')
