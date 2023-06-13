import torch
from transformers import BertModel, BertTokenizer, BertConfig


# Load the BERT tokenizer and configuration
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
config = BertConfig.from_pretrained('bert-base-multilingual-cased')
config.max_position_embeddings = 2048 # Increase the maximum sequence length
config.model_max_length = 2048 

# Load the BERT model with the modified configuration
model = BertModel.from_pretrained('bert-base-multilingual-cased', config=config, ignore_mismatched_sizes=True)


def tokenize(data=None):
    print("STATUS: running tokenization")
    res = []
    for i in range(0, len(data)):
        vector = tokenize_one(data[i])

        res.append(vector)
    return res


def tokenize_one(record):
    text = record
    # print(text) 
    # Токенизация и пакетирование текстов
    tokenized_text = tokenizer.encode(text, add_special_tokens=True)

    max_len = len(tokenized_text)
    padded_text = tokenized_text + [0] * (max_len - len(tokenized_text))
    input_ids = torch.tensor([padded_text])

    # Get the vector representation of the text
    with torch.no_grad():
        outputs = model(input_ids)
        last_hidden_state = outputs[0][:, 0, :].numpy()
    

    return last_hidden_state[0]