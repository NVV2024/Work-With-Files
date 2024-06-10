#Задача №3. от 10.06.2024

#from pathlib import Path
import os
from typing import Dict, Any

files = {}
f_list = []
sorted_dict = {}

files_array = ['1.txt','2.txt']

def qaz(files_array):
    count = 0
    #sorted_dict = {}
    for file in files_array:
        with open(file, encoding='utf-8') as f:
            name = f.name
            list_list = [name]
            #print(name)
            text1 = f.readlines()
            list_list.append(len(text1))
            files[name] = len(text1)
    sorted_list = sorted(files.items(), key=lambda x: x[1])
    sorted_dict = dict(sorted_list)
    print(sorted_dict)
    return sorted_dict


#print(f_list)
    #file[name] = count

qaz(files_array)

#print(files)
#print(sorted_dict)


#name = os.path.basename(r'C:\python3\file.txt ')
    #file1 = f.read()
# with open('2.txt', encoding='utf-8') as f:
#     file2 = f.read()
# with open('3.txt', encoding='utf-8') as f:
#     file3 = f.read()

# files = [file1, file2, file3]
#
# for i in files:
#     print(len(i))