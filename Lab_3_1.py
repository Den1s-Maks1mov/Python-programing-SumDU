string = input("Введіть слово: ")
while (len(string) < 2):
    string = input("Введіть слово ще раз: ")
print("Передостанній символ:", string[-2])