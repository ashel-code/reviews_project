# Функция, вычисляющая расстояние Левенштейна между двумя строками s и t
def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    if m < n:
        s, t = t, s  # Меняем местами s и t, если s меньше t
        m, n = n, m
    if n == 0:
        return m
    previous_row = range(n + 1)  # Инициализируем первую строку расстояния
    for i, c1 in enumerate(s):
        current_row = [i + 1]
        for j, c2 in enumerate(t):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    distance = previous_row[-1]  # Вычисляем расстояние Левенштейна между s и t
    return distance / min(m, n) < 0.3


# Функция, удаляющая все цифры из строки
def remove_numbers(string):
 
    # Создаем пустую строку
    output_string = ""
 
    # Итерируемся по символам строки
    for char in string:
 
        # Проверяем, является ли символ буквой или пробелом
        if char.isalpha() or char == ' ':
            output_string += char
 
    # Возвращаем отфильтрованную строку
    return output_string


# Функция, считающая частоту встречаемости слов в тексте
def rate_words(text):
    words = text.split(' ')  # Разбиваем текст на слова

    res = []
    for word in words:
        for i in range(len(res)):
            # Если слово уже есть в списке, увеличиваем его счетчик
            if levenshtein_distance(word, res[i][1]):
                res[i][0] += 1
                break
        else:
            # Если слова нет в списке, добавляем его в список со счетчиком 1
            res.append([1, word])

    res.sort()  # Сортируем список по возрастанию частоты
    res.reverse()  # Разворачиваем список, чтобы получить частоты в порядке убывания
    return res
                
 
# Вызываем функции и выводим результаты

# text = "aaaa aaab a b a b b c c a c b"
text = '''
This is a sample text. It contains some words, some of which are repeated. 
This is just to test the rate_words function. The result should show each word and its frequency.
'''

text = remove_numbers(text)  # Удаляем цифры из текста

print(str(rate_words(text.lower())).replace("], [", "\n"), sep='\n')  # Выводим список слов и их частот, разделяя их переносом
