import tensorflow as tf
from get_config import get_data
from tokenizing import tokenize
import numpy as np



def predict(data):
    with tf.device('/cpu:0'):
        model_link = get_data('model_path')
        model =  tf.keras.models.load_model(model_link)
        
        neuro_res = []
    
        print("STATUS: model loaded")
        for text in data:
            lst = text.split(".", "\n")
            vector = tokenize(data=lst)
            

            vector = np.array(vector)
            vector = vector.reshape((len(vector), 24, 32))

            neuro_pre_res = model.predict(vector)
            r1 = np.average(neuro_pre_res)

            neuro_res.append(r1)

        return neuro_res