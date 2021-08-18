
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* numero):
    from time import sleep
    maiorNumero = max(numero)
    for valor in numero:
        sleep(0.5)
        print(f'{valor} ', end=' ► ')
    print('FIM!')
    print(f'O maior valor informado foi ► {maiorNumero}')
    print('—' * 50)


print('—' * 50)
print('Analisando os valores...')
maior(2, 1, 70, 224, 14, 158, 58)
print('Analisando os valores...')
maior(80, 0, 15, 255, 44, 258, 55)
print('Analisando os valores...')
maior(4, 4, 7, 6, 2, 5)
