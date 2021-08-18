
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.



numeros = list()

def sorteia():
    from random import randint

    for contador in range(0, 5):
        sorteio = randint(0, 10)
        numeros.append(sorteio)


def somaPar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma entre todos os valores pares é ► {soma}')


sorteia()
print('—' * 50)
print(f'Foram sorteados os valores ► {numeros}')
somaPar()
print('—' * 50)