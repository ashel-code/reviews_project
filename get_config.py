"""File to get info from config file"""
import json


FILE_NAME = 'config.json'  # Config file name

with open(FILE_NAME, encoding="utf-8") as json_file:  # Open json file
    file = json.load(json_file) 


def get_data(key):
    """
    Get info from config
    :param key: key from data dict("model_path")
    :return: value from config file
    """
    return file[key]
