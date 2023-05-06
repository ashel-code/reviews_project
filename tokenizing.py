import torch
from transformers import BertModel, BertTokenizer, BertConfig
import numpy as np
from structure.unvectorized_data import Unvectorized



def tokenize():
    # TODO: data = database.getUnvectorized()

    data = [Unvectorized(1, 'какая я то умная шиза длиннее чем ноль и больше чем нечто другое вот'),
      Unvectorized(5, 'текст  просто текст без знаков препинания'),
      Unvectorized(12, 'помогите мне пожалуйста'),
      Unvectorized(33, 'я так устал кодить что то что я не понимаю'),]
    
    tokenize(data)


def tokenize(data):
    # Load the BERT tokenizer and configuration
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    config = BertConfig.from_pretrained('bert-base-multilingual-cased')
    config.max_position_embeddings = 1024 # Increase the maximum sequence length


    # Load the BERT model with the modified configuration
    model = BertModel.from_pretrained('bert-base-multilingual-cased', config=config, ignore_mismatched_sizes=True)
    
    # Список текстов для обработки
    texts = [d.text for d in data]

    # Токенизация и пакетирование текстов
    tokenized_texts = [tokenizer.encode(text, add_special_tokens=True) for text in texts]
    max_len = max(len(text) for text in tokenized_texts)
    padded_texts = [text + [0] * (max_len - len(text)) for text in tokenized_texts]
    input_ids = torch.tensor(padded_texts)

    # Получение векторных представлений текстов
    with torch.no_grad():
        outputs = model(input_ids)
        last_hidden_states = outputs[0][:, 0, :].numpy()
    

    np.savetxt('vector.txt', last_hidden_states)
    for i in range(len(last_hidden_states)):
        pass
        # TODO: database.addVector(i, last_hidden_states[i])

