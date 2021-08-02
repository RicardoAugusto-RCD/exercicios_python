
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

contador = frase.count('A')
print('A letra "A" aparece {}x.'.format(contador))

primeira = frase.find('A')
print('A primeira letra "A" foi encontrada na posição {}'.format(primeira + 1))

ultima = frase.rfind('A')
print('A última letra "A" foi encontrada na posição {}'.format(ultima + 1))