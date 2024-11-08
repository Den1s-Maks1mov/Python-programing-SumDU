import matplotlib.pyplot as plt
import numpy as np
import json

# зчитування даних з файлу
try:
    with open('Lab12_people.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Файл Lab12_people.json не знайдено.")

# підрахунок кількості чоловіків та жінок
maleCount = sum(1 for people in data.values() if people["Стать"] == "чоловіча")
femaleCount = sum(1 for people in data.values() if people["Стать"] == "жіноча")

# дані для побудови діаграми
labels = ['Чоловіки', 'Жінки']
sizes = np.array([maleCount, femaleCount])
colors = ['blue', 'pink']

# побудова кругової діаграми
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis("equal")
plt.title('Співвідношення чоловіків та жінок')
plt.legend(labels)
plt.show()