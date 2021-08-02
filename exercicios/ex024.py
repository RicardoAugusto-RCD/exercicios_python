
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: ')).strip().capitalize()

santo = cidade[:5] == 'Santo'

print('O nome da cidade possui Santo? ')
print(santo)
