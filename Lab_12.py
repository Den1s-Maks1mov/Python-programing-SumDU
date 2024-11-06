import json

# функція для зчитування даних з JSON файлу
def LoadData(filename="Lab12_people.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return {}

# функція для запису даних в JSON файл
def SaveData(data, filename="Lab12_people.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("Дані збережено у файл.")

# функція для виведення всіх даних з JSON файлу
def PrintData(data):
    for key, value in data.items():
        print(f"{key}: зріст - {value['Зріст']}, стать - {value['Стать']}")

# функція для додавання нового запису в JSON файл
def Add(data, name, height, gender):
    data[name] = {"Зріст": height, "Стать": gender}
    print(f"Додано {name}.")

# функція для видалення запису з JSON файлу
def Delete(data, name):
    if name in data:
        del data[name]
        print(f"Видалено {name}.")
    else:
        print(f"Особа {name} не знайдена.")

# функція для пошуку осіб за полем
def SearchPerson(data, field, value):
    results = {k: v for k, v in data.items() if v.get(field) == value}
    if results:
        for key, value in results.items():
            print(f"{key}: зріст - {value['Зріст']}, стать - {value['Стать']}")
    else:
        print("Нічого не знайдено.")

# функція для обчислення середнього зросту чоловіків і збереження результату в JSON файл
def AverageMaleHeight(data, filename="Lab12_average.json"):
    total_height = sum(person["Зріст"] for person in data.values() if person["Стать"] == "чоловіча")
    male_count = sum(1 for person in data.values() if person["Стать"] == "чоловіча")
    
    if male_count > 0:
        average_height = total_height / male_count
        result = {"Середній зріст чоловіків": round(average_height, 2)}
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)
        print(f"Середній зріст чоловіків: {average_height:.2f} см (збережено в {filename})")
    else:
        print("Чоловіків у списку немає.")

# реалізація функцій
data = LoadData()

print("\nЩоб вивести весь словник, натисніть -> 1 <-")
print("Щоб додати до словника елемент, натисніть -> 2 <-")
print("Щоб видалити із словника елемент, натисніть -> 3 <-")
print("Щоб знайти елемент за полем, натисніть -> 4 <-")
print("Щоб порахувати середній чоловічий зріст, натисніть -> 5 <-")
print("Щоб закрити програму, натисніть -> 6 <-")

while True:
    choice = input("\nВиберіть дію: ")
    if choice == "1":
       PrintData(data)
    elif choice == "2":
        name = input("Введіть ім'я та прізвище (приклад: Денис Максимов): ")
        height = int(input("Введіть зріст: "))
        gender = input("Введіть стать (чоловіча/жіноча): ")
        Add(data, name, height, gender)
        SaveData(data)
    elif choice == "3":
        name = input("Введіть ім'я та прізвище для видалення: ")
        Delete(data, name)
        SaveData(data)
    elif choice == "4":
        field = input("Введіть поле для пошуку (Зріст/Стать): ")
        value = input("Введіть значення для пошуку: ")
        SearchPerson(data, field, value)
    elif choice == "5":
        AverageMaleHeight(data)
    elif choice == "6":
        SaveData(data)
        print("Програма завершена.")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")