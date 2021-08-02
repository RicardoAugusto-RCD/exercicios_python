
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar:1

numero = int(input('Digite um número qualquer entre 0 e 9999: '))
print(numero)

unidade = numero % 10
print('Unidade {}'.format(unidade))

numero = (numero - unidade) / 10
dezena = numero % 10
print('Dezena {:.0f}'.format(dezena))

numero = (numero - dezena) / 10
centena = numero % 10
print('Centena {:.0f}'.format(centena))

numero = (numero - centena) / 10
milhar = numero % 10
print('Milhar {:.0f}'.format(milhar))