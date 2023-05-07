import sys
import json 
from parsing import parse
from tokenizing import tokenize
from clusterization import *

def main(args):
  
    # имя конфиг файла
    filename = 'config.json'
  
    # чтение аргумента с текстом (опционального)

    # открывает json файл
    with open(filename) as json_file: 
    # проверка достаточно ли аргументов
        if len(args) < 2:
            print("INFO: running without arguments")
            data = json.load(json_file) 
        
            parse(data['url'], data['page_path'])
        else:
            param = args[1]

            if param.contains('p'):
                parse(data['url'], data['page_path'])
            if param.contains('t'):
                tokenize()
            if param.contains('c'):
                # TODO: run clusterization
                pass 



# вызов основной функции
if __name__ == "__main__":
    main(sys.argv)
    main()
