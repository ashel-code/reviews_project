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


# вызов основной функции
if __name__ == "__main__":
    # main(sys.argv)
    main()
