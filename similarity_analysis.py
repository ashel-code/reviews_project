
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from get_config import read_list

print('Loading data...')
nltk.download('punkt')


from nltk import word_tokenize
def tokenizer(x):
    return (w for w in word_tokenize(x) if len(w) >3)

vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)

def binary_search(texts, x):
    left = 0
    right = len(texts) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if len(texts[mid]) == x:
            result = mid
            right = mid - 1  
        elif len(texts[mid]) < x:
            left = mid + 1
        else:
            right = mid - 1

    return result

def sentence_similarity(sentence1, sentence2):
    corpus = [sentence1, sentence2]

    # Преобразуем предложения в матрицу TF-IDF
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Вычисляем косинусное расстояние между предложениями
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return similarity


def find_max_similarity(text, texts):
    length = len(text)
    similarity = 0.0
    for i in range(binary_search(texts, length - 3),len(texts)):
        other_text = texts[i]
        if len(other_text) >= length + 3: 
            current_similarity = sentence_similarity(text, other_text)
            if current_similarity > similarity and current_similarity <= (0.98):
                    similarity = current_similarity

    return similarity


sorted_texts = read_list('./data/sorted_texts.bin')

def get_sim(text):
    find_max_similarity(text, sorted_texts)
