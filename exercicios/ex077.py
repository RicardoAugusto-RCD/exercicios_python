
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são suas vogais.

listaNomes = ('Ricardo', 'Marina', 'Henrique', 'Maria Eduarda', 'Marianna', 'Amanda')

print('—' * 50)

for nome in listaNomes:
    print(f'As vogais de {nome.upper()} são → ', end='')

    for letras in nome:

        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')
    print()

print('—' * 50)
