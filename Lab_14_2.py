import matplotlib.pyplot as plt
import numpy as np
import csv

years = []
ukraineValues = []
usaValues = []

# зчитування даних з CSV-файлу
try:
    with open('Lab14_2_file-data.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            if row[1] == 'UKR':
                ukraineValues = [float(value) for value in row[4:-1] if value]
                years = [int(year.split()[0]) for year in header[4:-1]]
            elif row[1] == 'USA':
                usaValues = [float(value) for value in row[4:-1] if value]

except FileNotFoundError:
    print("Помилка: Файл 'Lab14_2_file-data.csv' не знайдено.")

# перетворення списків на numpy масиви
x = np.array(years)
y = np.array(ukraineValues)
z = np.array(usaValues)

# функція будови графіку підзавдання 2.1
def Graph1(x, y, z):
    # побудова графіка
    plt.plot(x, y, label='Ukraine', color="purple")
    plt.plot(x, z, label='United States', color="yellow")

    # додавання заголовку та підписів до осей
    plt.title('Military Expenditure (% of GDP)', fontsize=15)
    plt.xlabel('Year', fontsize=12, color='red')
    plt.ylabel('Military Expenditure', fontsize=12, color='red')
    plt.legend()
    plt.grid(True)
    plt.show()

# функція будови графіку підзавдання 2.2
def Graph2(x, y, label, color):
    # побудова стовпчастої діаграми
    plt.bar(x, y, label=label, color=color)
    
    # додавання заголовку та підписів до осей
    plt.title(f'Military Expenditure (% of GDP) for {label}', fontsize=15)
    plt.xlabel('Year', fontsize=12, color='red')
    plt.ylabel('Indicator', fontsize=12, color='red')
    plt.legend()
    plt.grid(True)
    plt.show()

# реалізація функцій
print("---=== ОБЕРІТЬ ГРАФІК, ЯКИЙ ВИ ХОЧЕТЕ ПОБАЧИТИ ===---")
print("--> 1 <-- Побудова графіку одночасно двох країн")
print("--> 2 <-- Побудова стовпастої діаграми однієї з країн")
# вибір графіку для побудови
answer = int(input("Ви обрали графік - "))
if answer == 1:
    print("Графік підзавдання 2.1 побудовано успішно!")
    Graph1(x, y, z)
elif answer == 2:
    country = input("Введіть назву країни (Ukraine або United States): ")
    if country == "Ukraine":
        print("Діаграму підзавдання 2.2 побудовано успішно!")
        Graph2(x, y, "Ukraine", "purple")
    elif country == "United States":
        print("Діаграму підзавдання 2.2 побудовано успішно!")
        Graph2(x, z, "United States", "yellow")
    else:
        print("Помилка: Невідома країна.")
else:
    print("Обрано неправильне значення!")