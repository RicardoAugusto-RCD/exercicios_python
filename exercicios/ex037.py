
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 - Para binário
# 2 - Para octal
# 3 - Para hexadecimal

numero = int(input('Converta um número qualquer: '))

baseConversao = int(input('Digite 1 - Binário\nDigite 2 - Octal\nDigite 3 - Hexadecimal\nOpção: '))

if baseConversao == 1:
    binario = bin(numero)
    print('{} convertido para binário é igual a {}'.format(numero, binario[2:]))

elif baseConversao == 2:
    octal = oct(numero)
    print('{} convertido para octal é igual a {}'.format(numero, octal[2:]))

elif baseConversao == 3:
    hexadecimal = hex(numero)
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hexadecimal[2:]))

else:
    print('Opção inválida, tente novamente...')
