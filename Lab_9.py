# відкриття файлу і його перевірка на те, що він відкрився
def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print(f"Файл {file_name} не відкрився!")
        return None
    else:
        print(f"Файл {file_name} відкрився!")
        return file

file1_name = "TF16_1.txt"
file2_name = "TF16_2.txt"

# створення і запис у файл TF16_1
file_1_w = Open(file1_name, "w")
if file_1_w is not None:
    file_1_w.write("Python - інтерпретована об'єктно орієнтована мова програмування, яка є високого рівня.")
    print("Інформацію було додано до файлу TF16_1.txt!")
    file_1_w.close()
    print("Файл TF16_1.txt закрився!")

# читання з TF16_1 та запис слів, що починаються на голсну у TF16_2
file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")
vowels = {'А', 'Е', 'Є', 'И', 'І', 'Ї', 'О', 'У', 'Ю', 'Я', 
          'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я'}

if file_2_r is not None and file_2_w is not None:
    for block in file_2_r.read().split():
        word = block.strip(",.!?")
        if word and word[0] in vowels:
            file_2_w.write(word + '\n')
    file_2_r.close()
    file_2_w.close()
    print("Слова були записані до файлу TF16_2.txt, який потім закрився!")

# читання з TF16_2 та виведення по рядках
print("Вивід змісту файлу TF16_2.txt:")
file_3_r = Open(file2_name, "r")
if file_3_r is not None:
    for line in file_3_r:
        print(line.strip())
    print("Файл TF16_2.txt закрився!")
    file_3_r.close()
