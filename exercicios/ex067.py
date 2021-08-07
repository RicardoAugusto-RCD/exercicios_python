
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo.

separador = ('—' * 60)

while True:
    print(separador)
    n = int(input('Quer ver a tabuada de qual valor? [número negativo para sair]: '))

    if n >= 0:

        for c in range(1, 11):
            print(f'{n} x  {c} = {n*c}')

    else:
        break

print(separador)
print(f'PROGRAMA ENCERRADO')
print(separador)
