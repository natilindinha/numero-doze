n = 0
primos = 0
while n < 9:
    num = int(input('digite um numero:'))
    if num % 2 == 1 or num == 2:
        primos = primos + 1
    n = n + 1
print('a quantidade de numeros primos foram:', primos)
