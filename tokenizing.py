import torch
from transformers import BertModel, BertTokenizer, BertConfig
import numpy as np
from structure.unvectorized_data import Unvectorized
from db_actions import DatabaseActions as db


def tokenize():
    print("STATUS: running tokenization")
    data = db.get_unvectorized()

    tokenizeData(data)
 

def tokenizeData(data):
    # Load the BERT tokenizer and configuration
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    config = BertConfig.from_pretrained('bert-base-multilingual-cased')
    config.max_position_embeddings = 2048 # Increase the maximum sequence length
    config.model_max_length = 2048 

    # Load the BERT model with the modified configuration
    model = BertModel.from_pretrained('bert-base-multilingual-cased', config=config, ignore_mismatched_sizes=True)
    
    
    for i in range(0, len(data)):
        print('RUNNING', i + 1, '/', len(data), end='\r')
        tokenize_one(data[i], model, tokenizer)
    
    print('FINISHED', len(data), '/', len(data))


def tokenize_one(record, model, tokenizer):
    text = record.text
    # print(text)
    # Токенизация и пакетирование текстов
    tokenized_text = tokenizer.encode(text, add_special_tokens=True)
    # Tokenize and pad the text
    tokenized_text = tokenizer.encode(text, add_special_tokens=True)
    max_len = len(tokenized_text)
    padded_text = tokenized_text + [0] * (max_len - len(tokenized_text))
    input_ids = torch.tensor([padded_text])

    # Get the vector representation of the text
    with torch.no_grad():
        outputs = model(input_ids)
        last_hidden_state = outputs[0][:, 0, :].numpy()
    

    # np.savetxt('vector.txt', last_hidden_states)
    db.add_vector(record.id, last_hidden_state[0])
    # TODO: database.addVector(i, last_hidden_states[i])

