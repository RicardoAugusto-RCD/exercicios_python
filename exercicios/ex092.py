
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário,
# se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira Trabalho [0 não tem]: '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário R$ '))
    dados['aposentadoria'] = dados['contratacao'] - nascimento + 35

print('—' * 50)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
