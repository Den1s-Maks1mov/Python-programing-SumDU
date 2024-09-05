string = input("Введіть слово: ")
while (len(string) < 2):
    string = input("Введіть слово ще раз: ")
nonNumberString = ''.join(filter(str.isalpha, string))
print("Слово без цифр виглядає так:", nonNumberString)