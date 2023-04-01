# Импортируем библиотеки
import gensim
from gensim.models import Word2Vec
import nltk
nltk.download('punkt')

# Загружаем данные и проводим предобработку
data = "Пример текста, который нужно перевести в векторную форму."
sentences = nltk.sent_tokenize(data)
word_tokens = [nltk.word_tokenize(sentence) for sentence in sentences]

# Обучаем модель Word2Vec на предобработанных данных
model = Word2Vec(word_tokens, min_count=1)

# Получаем вектор для каждого слова
vectors = []
for word in word_tokens:
    vector = model.wv[word]
    vectors.append(vector)

print(vectors)