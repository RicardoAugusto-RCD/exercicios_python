
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um valor: '))

n2 = int(input('Digite outro valor: '))

opcao = 0

while opcao != 5:

    opcao = int(input('Digite [1] Somar [2] Multiplicar [3] Maior [4] Novos números [5] Sair do programa '))

    if opcao == 1:
        soma = n1 + n2
        print(soma)

    elif opcao == 2:
        multiplica = n1 * n2
        print(multiplica)

    elif opcao == 3:
        if n1 > n2:
            print(n1)
        elif n1 == n2:
            print('Iguais')
        else:
            print(n2)

    elif opcao == 4:
        n1 = int(input('Digite um valor: '))

        n2 = int(input('Digite outro valor: '))

    elif opcao == 5:
        print('Saindo...')

    else:
        print('VAI TOMAR NO CU, FDP!!!')




