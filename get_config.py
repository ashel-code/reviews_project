
import json
# имя конфиг файла
filename = 'config.json'

# открывает json файл
with open(filename) as json_file: 
    # проверка достаточно ли аргументов

    file = json.load(json_file) 

def data(s):
    return file[s]
