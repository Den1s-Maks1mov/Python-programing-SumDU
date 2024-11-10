import pandas as pd
import matplotlib.pyplot as plt

# список місяців
months = [
    "Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
    "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"
]

# завантаження даних з файлу
data = pd.read_csv('Lab15_2_data.csv')

# перетворення стовпця `Date` у формат інформації та виділення місяця
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
data['Month'] = data['Date'].dt.month
data['Total'] = data.iloc[:, 2:].sum(axis=1)
monthly_data = data.groupby('Month')['Total'].sum()

# знаходження найбільш популярного місяця
most_popular_month = monthly_data.idxmax()
print(f"Найбільш популярний місяць для велосипедистів у 2015 році: {months[most_popular_month - 1]}")

# побудова графіку використання велодоріжок по місяцях
plt.figure(figsize=(10, 6))
plt.bar(months, monthly_data)
plt.title("Динаміка за місяцями")
plt.xlabel("Місяці")
plt.ylabel("Значення")
plt.xticks(rotation=45)
plt.show()