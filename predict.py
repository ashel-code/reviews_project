import tensorflow as tf
from get_config import get_data
from tokenizing import tokenize
from frequency_analysis import get_prob
from similarity_analysis import get_sim

def get_model():
    model_link = get_data('model_path')
    # проверка достаточно ли аргументов
    return tf.keras.models.load_model(model_link)

def predict(data):
    model = get_model()
    vector = tokenize(data=data)
    
    neuro_res = model.predict(vector)

    # algo1_res = []
    # for i in range(len(data)):
    #     algo1_res.append(get_prob(data[i]))

    # algo2_res = []
    # for i in range(len(data)):
    #     algo2_res.append(get_sim(data[i]))


    # X = []
    # for i in range(len(data)):
    #     X.append([neuro_res[i], algo1_res[i], algo2_res[i]])

    return neuro_res