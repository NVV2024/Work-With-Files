f = open('recipes.txt', encoding='utf-8')
data = f.read()
f.close()

cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    count =0
    nn = 0
    for line in f:
        count +=1
        #Считаем длинну строки "l="
        l = len(line.strip())
        str_name = line.strip()
        print(count, str_name)
        #print("Длинна строки:",l,"\n")

        if count == 1:    #Определяем ключ словаря и создаём словарь
            cook_book[str_name] = []
            nn +=1
            list_name_temp = []
            # print(type(list_name_temp))
            # list_name = list(list_name_temp)
            # print(list_name)

        elif count == 2:    #Формируем значеия словаря
            recip_len = int(str_name)
        elif recip_len-1 < count > 2:
            #cook_book[str_name].append() = str_name
            #pass
            list_name_temp.append(str_name)
        cook_book[str_name] = list_name_temp

        #Вычисляем пробелы в рецепте
        if len(line.strip()) == 0:
            count=0
print()
print(cook_book)
print('Размер рецепта:', count, "строк")
#
# for l in data:
#     print(l)

