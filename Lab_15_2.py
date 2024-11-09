import pandas as pd
import matplotlib.pyplot as plt

# завантаження даних з файлу
data = pd.read_csv('Lab15_2_data.csv')

# перетворення стовпця `Date` у формат інформації та виділення місяця
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
data['Month'] = data['Date'].dt.month
data['Total'] = data.iloc[:, 2:].sum(axis=1)
monthly_data = data.groupby('Month')['Total'].sum()

# знаходження найбільш популярного місяця
most_popular_month = monthly_data.idxmax()
print(f"Найбільш популярний місяць для велосипедистів у 2015 році: {most_popular_month}")

# побудова графіку використання велодоріжок по місяцях
plt.figure(figsize=(10, 6))
monthly_data.plot(kind='bar', color='skyblue')
plt.title('Використання велодоріжок по місяцях у 2015 році')
plt.xlabel('Місяць')
plt.ylabel('Загальна кількість велосипедистів')
plt.xticks(rotation=0)
plt.show()