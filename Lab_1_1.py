print("*Діапазон цілих чисел від 1 до 10*")
a = int(input("Введіть додатнє число a: "))
b = int(input("Введіть додатнє число b: "))
if a > b:
    X = b / a + 61
elif a == b:
    X = -5
else:
    X = (b - a) / b
print("X =", X)