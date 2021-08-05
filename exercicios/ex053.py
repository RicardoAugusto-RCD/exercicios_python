
# Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços.

fraseOriginal = str(input('Escreva uma frase: '))

fraseManipulada = fraseOriginal.replace(" ", "")

fraseInvertida = fraseManipulada[::-1]

print('A frase {}{}{}, forma um palíndromo? '.format('\033[034m', fraseOriginal,  '\033[m'), end="")

if fraseManipulada == fraseInvertida:
    print('\033[031mSIM')

else:
    print('\033[031mNÃO')