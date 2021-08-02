
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas letras maiúsculas.
# O nome com todas letras minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nomeCompleto = str(input('Digite seu nome completo: ')).strip()

nomeMaiusculo = nomeCompleto.upper()
print('{} com todas as letras maiúsculas: {}'.format(nomeCompleto, nomeMaiusculo))

nomeMinusculo = nomeCompleto.lower()
print('{} com todas as letras minúsculas: {}'.format(nomeCompleto, nomeMinusculo))

nomeTotal = nomeCompleto.replace(' ', '')
print('{} tem o total de {} letras, sem considerar os espaços'.format(nomeCompleto, len(nomeTotal)))

primeiroNomeTotal = nomeCompleto.find(' ')
print('{} tem o total de {} letras, em seu primeiro nome'.format(nomeCompleto, primeiroNomeTotal))


