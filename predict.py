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
        ln = len(data)
        for i in range(ln):
            text = data[i]
            print('RUNNING', i + 1, '/', ln, end='\r')
            lst = text.split(".\n!)(?")
            vector = tokenize(data=lst)
            

            vector = np.array(vector)
            vector = vector.reshape((len(vector), 24, 32))


            neuro_pre_res = model.predict(vector)
            r = 0
            for i in range(len(neuro_pre_res)):
                r += neuro_pre_res[i] * len(lst[i])
            
            r /= (len(text) * len(neuro_pre_res))

            neuro_res.append(float(r))

        return neuro_res