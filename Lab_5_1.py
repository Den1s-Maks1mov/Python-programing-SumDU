n = int(input("n = "))
print(f"Введіть {n} елементів:")
arr = [int(input()) for _ in range(n)]
positive_elements = [num for num in arr if num > 0]
if positive_elements:
    min_positive = min(positive_elements)
    print("Мінімальний додатній елемент:", min_positive)
else:
    print("Додатніх елементів немає")
