
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numero = (int(input('Digite o 1º número: ')),
          int(input('Digite o 2º número: ')),
          int(input('Digite o 3º número ')),
          int(input('Digite o 4º número ')))
print('—' * 50)

print(f'Você digitou os valores {numero}')
print('—' * 50)

print(f'O valor 9 apareceu {numero.count(9)} vezes')
print('—' * 50)

if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3) + 1}ª posição')
    print('—' * 50)
else:
    print('Valor 3 não foi digitado em nenhuma posição')
    print('—' * 50)

print(f'Os valores pares digitados foram ', end='')
for num in numero:
    if num % 2 == 0:
        print(num, end=' ')
print()
print('—' * 50)
