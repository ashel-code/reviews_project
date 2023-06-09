import tensorflow as tf
from get_config import get_data
from tokenizing import tokenize
import numpy as np

def get_model():
    model_link = get_data('model_path')
    # проверка достаточно ли аргументов
    return tf.keras.models.load_model(model_link)

def predict(data):
    model = get_model()
    
    print("STATUS: model loaded")
    vector = tokenize(data=data)
    vector = np.array(vector)
    vector = vector.reshape((len(vector), 24, 32))
    neuro_res = model.predict(vector)

    return neuro_res