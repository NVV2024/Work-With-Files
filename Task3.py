#Задача №3. от 10.06.2024

#from pathlib import Path
import os

count = 0

with open('1.txt', encoding='utf-8') as f:
    text1 = f.read().split(" ")
    name = f.name
    for line in f:
        count += 1
        #pass

print(name)
print(count)
print(text1)

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