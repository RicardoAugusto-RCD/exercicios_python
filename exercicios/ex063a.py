n = int(input('Quantos termos de uma Sequência de Fibonacci você quer ver? '))

t1 = 0
t2 = 1

while n != 0:
    print(t1, end=' ► ')

    t3 = t1 + t2
    t1 = t2
    t2 = t3
    n -= 1

print('FIM', end='')