
# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior v da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaColuna = maiorValor = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        valores = int(input(f'Digite um valor para {[linha, coluna]}: '))
        matriz[linha][coluna] = valores

        if valores % 2 == 0:
            somaPares += valores

        if coluna == 2:
            somaColuna += valores

        if linha == 1:
            if coluna == 0:
                maiorValor = valores
            else:
                if valores > maiorValor:
                    maiorValor = valores

print('—' * 50)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^10}]', end='')
    print()

print('—' * 50)

print(f'A soma de todos os valores pares é {somaPares}')
print(f'A soma de todos os valores da terceira coluna é {somaColuna}')
print(f'O maior valor da segunda linha é {maiorValor}')

print('—' * 50)