
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Escreva em metros e descubra sua conversão para centímetros e milímetros:'))

km = m / 1000
hec = m / 100
dam = m / 10
dec = m * 10
cm = m * 100
mm = m * 1000

print('{}m equivalem à {}km, {}hec, {}dam, {}dec, {}cm e {}mm'.format(m, km, hec, dam, dec, cm, mm))

