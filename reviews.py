import sys
from parse_script import parse
import json 

def main():
  
    # имя конфиг файла
    filename = 'config.json'
  
    # открывает json файл
    with open(filename) as json_file: 
        # загружаем данные  
        data = json.load(json_file) 
    
        parse(data['url'], data['page_path'])


    # # проверка достаточно ли аргументов
    # if len(args) < 2:
    #     raise Exception("Not enough arguments provided")
 
    # # чтение аргумента с текстом (опционального)
    # some_text = args[1]
 
    # # теперь можно что-то делать с текстом
    # print(some_text)
 
# вызов основной функции
if __name__ == "__main__":
    # main(sys.argv)
    main()
