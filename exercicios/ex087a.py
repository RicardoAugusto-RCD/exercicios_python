
# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior v da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = maiorValor = somaColuna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('—' * 50)

for linha in range(0,3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^10}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
    print()

print('—' * 50)

print(f'A soma dos valores pares é {somaPares}')

for linha in range(0, 3):
    somaColuna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somaColuna}')

for coluna in range(0, 3):
    if coluna == 0:
        maiorValor = matriz[1][coluna]
    elif matriz[1][coluna] >  maiorValor:
        maiorValor = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maiorValor}')

print('—' * 50)
