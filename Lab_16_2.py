import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# завантаження ненобхідних команд та даних
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# відкриття файлу
try:
    with open('Lab16_2_old-text.txt', 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

# інііалізація токенізації, лемматизації, стенммера
tokens = word_tokenize(text)
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# видалення пунктуації і стоп-слів, лемматизація та стеммінг
stop_words = set(stopwords.words('english'))
processed_tokens = []
for token in tokens:
    if token not in string.punctuation:
        if token.lower() not in stop_words:
            lemma = lemmatizer.lemmatize(token.lower())
            stemmed = stemmer.stem(lemma)
            processed_tokens.append(stemmed)
processed_text = ' '.join(processed_tokens)

# запис обробленого тексту в новий файл
with open('Lab16_2_new-text.txt', 'w', encoding='utf-8') as file:
    file.write(processed_text)

print("Обробка тексту завершена, результат записано у файл Lab16_2_new-text.txt.")