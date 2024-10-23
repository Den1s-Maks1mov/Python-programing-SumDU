# оголошення словника з 10 осіб
people = {
    "Артем_Пивоваров":{"Зріст": 170, "Стать":"чоловіча"},
    "Злата_Огнєвіч":{"Зріст": 165, "Стать":"жіноча"},
    "Оля_Полякова":{"Зріст": 180, "Стать":"жіноча"},
    "Дмитро_Монатік":{"Зріст": 164, "Стать":"чоловіча"},
    "Надія_Дорофєєва":{"Зріст": 168, "Стать":"жіноча"},
    "Святослав_Вакарчук":{"Зріст": 176, "Стать":"чоловіча"},
    "Настя_Каменських":{"Зріст": 175, "Стать":"жіноча"},
    "Наталія_Могилевська":{"Зріст": 162, "Стать":"жіноча"},
    "Павло_Зібров":{"Зріст": 190, "Стать":"чоловіча"},
    "Тарас_Тополя":{"Зріст": 177, "Стать":"чоловіча"},
}

# функція виводу всього словника
def Print(people):
    for i in people:
        print(f"  {i}: зріст - {people[i]['Зріст']}, стать - {people[i]['Стать']}")

# функція для додавання нової людини
def Add(people, key, height, gender):
    people[key] = {'Зріст': height, 'Стать': gender}
    print(f"Добавлено {key}.")

# функція для видалення людини
def Delete(people, key):
    if key in people:
        del people[key]
        print(f"Видалено {key}.")
    else:
        print(f"Особа {key} не знайдена.")

# функція сортування всіх людей за іменем
def PrintSort(people):
    sorted_people = {k: people[k] for k in sorted(people)}
    print("Відсортований список осіб:")
    for i in sorted_people:
        print(f"{i}: зріст - {people[i]['Зріст']}, стать - {people[i]['Стать']}")

# функція пошуку середнього арифметичного зросту всіх чоловіків
def AverageMaleHeight(people):
    total_height = 0
    male_count = 0 
    for i in people:
        if people[i]['Стать'] == 'чоловіча':
            total_height += people[i]['Зріст']
            male_count += 1
    if male_count > 0:
        average_height = total_height / male_count
        print(f"Середній зріст чоловіків: {average_height:.2f} см")
    else:
        print("Чоловіків у списку немає.")

# реалізація всіх функцій
print("Щоб вивести весь словник, натисніть -> 1 <-")
print("Щоб додати до словника елемент, натисніть -> 2 <-")
print("Щоб видалити із словника елемент, натисніть -> 3 <-")
print("Щоб відсортувати словник за іменами, натисніть -> 4 <-")
print("Щоб порахувати середній чоловічий зріст, натисніть -> 5 <-")
print("Щоб закрити програму, натисніть -> 6 <-")
while True:
    answer = int(input("\nВи обираєте дію - "))
    if(answer==1):
        Print(people)
    elif(answer==2):
        key = str(input("Введіть ім'я та прізвище (приклад: Денис_Максимов) - "))
        height = int(input("Введіть зріст - "))
        gender = str(input("Введіть стать (приклад: чоловіча або жіноча) - "))
        Add(people, key, height, gender)
    elif(answer==3):
        key = str(input("Введіть ім'я та прізвище (приклад: Денис_Максимов) - "))
        Delete(people, key)
    elif(answer==4):
        PrintSort(people)
    elif(answer==5):
        AverageMaleHeight(people)
    elif(answer==6):
        break
    else:
        print("Вибрана неіснуюча дія.")