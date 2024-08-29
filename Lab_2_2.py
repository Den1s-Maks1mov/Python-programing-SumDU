from Mod_Lab_2_2 import product

N = int(input("Введіть значення N, що більше ніж 1: "))

while (N < 1):

    N = int(input ("Введіть ще раз N: "))

print ("Сума квадратів чисел від 1 до", N, "=", product(N))