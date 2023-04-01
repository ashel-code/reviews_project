from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np 

# Загрузка предобученной модели и токенизатора
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
model = AutoModel.from_pretrained("bert-base-multilingual-cased")

# Входной текст
text = '''
28 Ну, что ж! Очередное место в Москве с отличной локацией, отличным названием, отличной идеей и концепцией, НО хамским неадекватным персоналом, демонстративно держащим перед тобой какую-то папку с  мятой бумагой, с перечеркнутыми именами. И вот этот вот малообразованное провинциальное хамло, пытается изобразить из себя винный уютный ресторан. Качество еды и выбор вина отвратительный! Никому не советую это место, хотя чисто из-за расположения и отсутствия конкуренции, клиентов, видимо, хватает. Но, это совсем другая и только московская история!
'''

# Токенизация текста
tokens = tokenizer.encode(text, add_special_tokens=True)

# Преобразование токенов в тензор
tensor = torch.tensor([tokens])

# Прохождение тензора через модель для получения вектора
with torch.no_grad():
    output = model(tensor)

# Извлечение вектора из выходных данных модели
vector = output[0][0]

# Вывод вектора
# Преобразование тензора в массив NumPy
vector_np = vector.numpy()

# Установка опции вывода массива
np.set_printoptions(threshold=np.inf)

# Вывод массива
np.savetxt('vec.temp', vector_np)
print("finished")

import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Сокращение размерности вектора с помощью t-SNE
tsne = TSNE(n_components=2, random_state=42)
vector_tsne = tsne.fit_transform(vector_np)

# Визуализация вектора
plt.scatter(vector_tsne[:,0], vector_tsne[:,1])
plt.show()