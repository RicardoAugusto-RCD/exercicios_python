
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o nome: ')).strip()

nomePossuiSilva = 'silva' in nome.lower()

print('O nome digitado tem Silva?')
print(nomePossuiSilva)
