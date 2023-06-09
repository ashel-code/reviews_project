
import json
import pickle5 as pickle

# имя конфиг файла
filename = 'config.json'

# открывает json файл
with open(filename) as json_file: 
    # проверка достаточно ли аргументов

    file = json.load(json_file) 

def get_data(s):
    return file[s]


def read_list(path):
    with open(path, 'rb') as fp:
        n_list = pickle.load(fp)
        return n_list

def write_list(a_list, path):
    # store list in binary file so 'wb' mode
    with open(path, 'wb') as fp:
        pickle.dump(a_list, fp)
        print('Done writing list into a binary file')

