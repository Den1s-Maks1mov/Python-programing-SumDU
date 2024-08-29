import math

def expression (x,y):

    z = math.cos(x)**2+math.sin(y)**2

    return z

def product (N):

    S = 0

    for i in range (1, N + 1):

        S += i**2

    return S

x = int(input("Введіть значення x: "))

y = int(input("Введіть значення y: "))

print ("Значення виразу z = ", expression(x,y))

N = int(input("Введіть значення N, що більше ніж 1: "))

while (N < 1):

    N = int(input ("Введіть ще раз N: "))

print ("Сума квадратів чисел від 1 до", N, "=", product(N))