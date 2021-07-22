
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis
# sobre ele.

print('-'*20)

leia = input('Escreva algo: ')
print('-'*20)

print('O tipo primitivo do valor {} é'.format(leia), type(leia))
print('-'*20)

print('{}, é um múmero?'.format(leia), leia.isnumeric())

print('-'*20)
print('{}, é um digito?'.format(leia), leia.isdigit())

print('-'*20)
print('{}, é alfabético?'.format(leia), leia.isalpha())

print('-'*20)
print('{}, é alfanumérico?'.format(leia), leia.isalnum())

print('-'*20)
print('{}, está em maiúsculas?'.format(leia), leia.isupper())

print('-'*20)
print('{}, está em minúsculas?'.format(leia), leia.islower())

print('-'*20)
print('{}, só tem espaços?'.format(leia), leia.isspace())

print('-'*20)
print('{}, está capitalizada?'.format(leia), leia.istitle())

print('-'*20)
print('{}, é imprimível?'.format(leia), leia.isprintable())

print('-'*20)





