import tensorflow as tf
from get_config import data
from tokenizing import tokenize
from frequency_analysis import get_prob

def get_model():
    model_link = data('model_path')
    # проверка достаточно ли аргументов
    return tf.keras.models.load_model(model_link)

def predict(data):
    model = get_model()
    vector = tokenize(data=data)
    
    neuro_res = model.predict(vector)

    algo_res = []
    for i in range(len(data)):
        algo_res.append(get_prob(data[i]))

    