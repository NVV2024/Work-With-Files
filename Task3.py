#Задача №3. от 12.06.2024

#from pathlib import Path
import os
from typing import Dict, Any
import pprint

files = {}
f_list = []
sorted_dict = {}

files_array = ['1.txt','2.txt', '3.txt']

def prepare_text(files_array):
    count = 0
    for file in files_array:
        with open(file, encoding='utf-8') as f:
            name = f.name
            list_list = [name]
            text1 = f.readlines()
            list_list.append(len(text1))
            files[name] = len(text1)
    sorted_list = sorted(files.items(), key=lambda x: x[1])
    for i in sorted_list:
        with open(i[0], encoding='utf-8') as f1:
            text = f1.read()
            print(i[0])
            print(i[1])
            print(text, '\n')
    return sorted_dict

prepare_text(files_array)