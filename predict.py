import tensorflow as tf
from get_config import get_data
from tokenizing import tokenize
import numpy as np
import re



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
            text = text.replace('\n', '.')
            text = text.replace('!', '.')
            text = text.replace(')', '.')
            text = text.replace(')', '.')
            text = text.replace('?', '.')
            
            lst = text.split('.')

            vector = tokenize(data=lst)
            

            vector = np.array(vector)
            vector = vector.reshape((len(vector), 24, 32))


            neuro_pre_res = model.predict(vector)
            r = 0
            for j in range(len(neuro_pre_res)):
                print(lst[j] + "\n") 
                r += neuro_pre_res[j] * len(lst[j])
            
            r /= len(text)

            neuro_res.append(float(r))

        return neuro_res