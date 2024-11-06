import csv

# перевірка на відкрити файл та вивести всі дані для США та України за 2010-2019 роки
try:
    with open("Lab11_file-data.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)

        print("Country Name | Year | Inflation (%)")

        usaData = {}
        ukraineData = {}

        for row in reader:
            if row['Country Name'] == "United States" and row['Series Name'] == "Inflation, consumer prices (annual %)":
                for year in range(2010, 2020):
                    usaData[year] = float(row[f"{year} [YR{year}]"])
                    print(f"United States | {year} | {usaData[year]}")
            elif row['Country Name'] == "Ukraine" and row['Series Name'] == "Inflation, consumer prices (annual %)":
                for year in range(2010, 2020):
                    ukraineData[year] = float(row[f"{year} [YR{year}]"])
                    print(f"Ukraine | {year} | {ukraineData[year]}")

except FileNotFoundError:
    print("Файл Lab11_file-data.csv не знайдено!")

# порівняння показників для США та України і запис результатів у новий файл
try:
    with open("Lab11_comparison.csv", "w", newline="") as csvfile2:
        writer = csv.writer(csvfile2, delimiter=";")
        writer.writerow(["Year", "USA Inflation (%)", "Ukraine Inflation (%)", "Difference (%)"])

        for year in range(2010, 2020):
            if year in usaData and year in ukraineData:
                difference = usaData[year] - ukraineData[year]
                writer.writerow([year, usaData[year], ukraineData[year], abs(difference)])
                print(f"Year: {year}, USA Inflation: {usaData[year]}, Ukraine Inflation: {ukraineData[year]}, Difference: {difference}")

    print("Результати порівняння збережено у файлі Lab11_comparison.csv.")

except Exception as e:
    print(f"Сталася помилка: {e}")
