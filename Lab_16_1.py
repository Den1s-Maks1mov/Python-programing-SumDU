import nltk
import string
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# завантаження ненобхідних команд та даних
nltk.download("stopwords")
nltk.download("punkt")

# відкриття файлу
try:
    with open('melville-moby_dick.txt', 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

# токенізація по реченнях і підрахунок слів
sentences = nltk.sent_tokenize(text)
total_words = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences)
print(f"Загальна кількість слів у тексті: {total_words}")

# підрахунок найуживаніших слів до очищення
words = text.split()
word_counts = Counter(words)
most_common_words = word_counts.most_common(10)
print("\n---=== 10 найбільш вживаних слів у тексті (до очищення):\n", most_common_words)

# побудова графіка найуживаніших слів до очищення
x = [word for word, count in most_common_words]
y = [count for word, count in most_common_words]
plt.figure(figsize=(10, 5))
plt.bar(x, y)
plt.title("10 найбільш вживаних слів у тексті (до очищення)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()

# видалення пунктуації та стоп-слів
stop_words = set(stopwords.words("english"))
words_cleaned = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

# підрахунок найуживаніших слів після очищення
freq_dist_cleaned = FreqDist(words_cleaned)
most_common_words_cleaned = freq_dist_cleaned.most_common(10)
print("\n---=== 10 найбільш вживаних слів (після очищення):\n", most_common_words_cleaned)

# побудова графіка н айуживаніших слів після очищення
plt.figure(figsize=(10, 5))
plt.bar([word for word, count in most_common_words_cleaned], [count for word, count in most_common_words_cleaned])
plt.title("10 найбільш вживаних слів (після очищення)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()
