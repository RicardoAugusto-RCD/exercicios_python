
# Refaça o desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

primeiro = int(input('Primeiro termo: '))

razao = int(input('Razão da PA: '))

ultimo = primeiro + (10 - 1) * razao

while primeiro <= ultimo:

    print('{} ► '.format(primeiro), end='')

    primeiro += razao

print('FIM')


