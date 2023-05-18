import sys
import json 
from parsing import parse
from tokenizing import tokenize
from clusterization import *
from get_config import data

def main(args):

    # проверка достаточно ли аргументов
        if len(args) < 2:
            print("INFO: running without arguments")
        
            parse(data('url'), data('page_path'))
            tokenize()
            # TODO: run clusterization

        else:
            param = args[1]

            if 'p' in param:
                parse(data('url'), data('page_path'))
            if 't' in param:
                tokenize()
            if 'c' in param:
                # TODO: run clusterization
                pass 


# вызов основной функции
if __name__ == "__main__":
    main(sys.argv)

