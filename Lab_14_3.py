import json
import matplotlib.pyplot as plt

# зчитування даних з файлу Data.json
try:
    with open('Lab12_people.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Файл Lab12_people.json не знайдено.")

# підрахунок кількості чоловіків та жінок
male_count = sum(1 for person in data.values() if person["Стать"] == "чоловіча")
female_count = sum(1 for person in data.values() if person["Стать"] == "жіноча")

# дані для побудови діаграми
labels = ['Чоловіки', 'Жінки']
sizes = [male_count, female_count]
colors = ['blue', 'pink']

# побудова кругової діаграми
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Співвідношення чоловіків та жінок')
plt.show()