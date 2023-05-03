import torch
from transformers import BertModel, BertTokenizer, BertConfig
import matplotlib.pyplot as plt
import clusterization as cl

def tok(texts):
    for i in range(len(texts)):
        print(i, texts[i])
    # Загрузка модели BERT и токенизатора
    # model = BertModel.from_pretrained('bert-base-multilingual-cased')
    # tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

    # Load the BERT tokenizer and configuration
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    config = BertConfig.from_pretrained('bert-base-multilingual-cased')
    config.max_position_embeddings = 1024 # Increase the maximum sequence length


    # Load the BERT model with the modified configuration
    model = BertModel.from_pretrained('bert-base-multilingual-cased', config=config, ignore_mismatched_sizes=True)
    # Список текстов для обработки
    

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
    print(len(texts))

    for i, text in enumerate(texts):
        print(i)
        ax.scatter(last_hidden_states[i, 0], last_hidden_states[i, 1], label=i)
        
        ax.annotate(str(i), (last_hidden_states[i, 0], last_hidden_states[i, 1]))

    ax.legend()
    
    plt.ion()
    plt.show()


    print("PLT DONE")
    cl.cluster(texts)
    
    
