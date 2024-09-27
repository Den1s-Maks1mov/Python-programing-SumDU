# ФУНКЦІЯ ДЛЯ ЗАВДАННЯ 1
def task1():
  A = list(input("Введіть слова через пробіл: ").split())
  i = 0
  # Цикл для вставкинових елементів
  while i < len(A):
      element = input(f"Введіть новий елемент для вставки на позицію {i}: ")
      A.insert(i, element)
      i += 2
  print("Оновлений першою функцією список:", A)

# ФУНКЦІЯ ДЛЯ ЗАВДАННЯ 2
def task2():
  B = list(input("Введіть слова через пробіл: ").split())
  # Перевірка, чи не один елемент у списку
  if len(B) < 2:
    print("Заданий список не підходить для заданої функції!")
    return
  # Прохід по індексах від 0 до передостаннього з кроком 2
  for i in range(0, len(B) - 1, 2):
    # Перетасовка елементів з парним індексом i та наступний за ним
    B[i], B[i + 1] = B[i + 1], B[i]
  print("Оновлений другою функцією список: ", B)

# ФУНКЦІЯ ДЛЯ ЗАВДАННЯ 3
def task3():
  C = input("Введіть слова через пробіл: ")
  listX = C.lower().split()  # Перетворення до нижнього регістру і ділення на слова
  letter_count = {}
  # Прохід по кожному слову і кожній літері
  for word in listX:
      for letter in word:
          if letter in letter_count:
              letter_count[letter] += 1
          else:
              letter_count[letter] = 1
  # Знаходження всіх літер, які входять не менше двох разів
  С = {letter for letter, count in letter_count.items() if count >= 2}
  # Вивод множин літер
  print("Оновлений третьою функцією множина: ", С)

# ФУНКЦІЯ ДЛЯ ВИБОРУ ЗАВДАННЯ
def choice():
  answer = input("\nОБЕРІТЬ ФУНКЦІЮ 1, 2 ЧИ 3: ")
  if answer == "1":
    task1()
    choice()
  elif answer == "2":
    task2()
    choice()
  elif answer == "3":
    task3()
    choice()
  else:
    print("Неправильний вибір!")
    choice()

# ЗАПУСК ПРОГРАМИ
choice()