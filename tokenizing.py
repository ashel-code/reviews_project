import torch
from transformers import BertModel, BertTokenizer
import matplotlib.pyplot as plt

def tok(texts):
    # Загрузка модели BERT и токенизатора
    model = BertModel.from_pretrained('bert-base-multilingual-cased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

    # Список текстов для обработки
    
    print(texts)

    # Токенизация и пакетирование текстов
    tokenized_texts = [tokenizer.encode(text, add_special_tokens=True) for text in texts]
    max_len = max(len(text) for text in tokenized_texts)
    padded_texts = [text + [0] * (max_len - len(text)) for text in tokenized_texts]
    input_ids = torch.tensor(padded_texts)

    # Получение векторных представлений текстов
    with torch.no_grad():
        outputs = model(input_ids)
        last_hidden_states = outputs[0][:, 0, :].numpy()
    
    # for i, text in enumerate(texts):
    #     print(f"Вектор текста {i+1}: {last_hidden_states[i].tolist()}")

    # Визуализация векторов
    fig, ax = plt.subplots()
    for i, text in enumerate(texts):
        ax.scatter(last_hidden_states[i, 0], last_hidden_states[i, 1], label=i)
    ax.legend()
    plt.show()
