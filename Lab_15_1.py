import json
import pandas as pd

# зчитування даних з файлу
try:
    with open('Lab12_people.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Файл Lab12_people.json не знайдено.")

# створення DataFrame з отриманого словника
df = pd.DataFrame.from_dict(data, orient="index")

# виведення початкового DataFrame на екран
print("Початковий DataFrame:")
print(df)

# виконання агрегації та групування
grouped = df.groupby("Стать").agg(
    середній_зріст=("Зріст", "mean"),
    кількість=("Зріст", "size")
)

# виведення результатів
print("\nАгрегація за статтю (середній зріст і кількість):")
print(grouped)