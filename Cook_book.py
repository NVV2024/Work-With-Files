# f = open('recipes.txt', encoding='utf-8')
# data = f.read()
# f.close()

cook_book = {}
list_name_temp = []
dish_name = []
count = 0
nn = 0

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        count += 1
        # Считаем длинну строки "l="
        l = len(line.strip())
        str_name = line.strip()
        print(count, str_name)
        # zipped = zip(count, str_name)
        # print("Длинна строки:",l,"\n")

        if count == 1:  # Определяем ключ словаря и добавляем его словарь
            # cook_book[str_name] = []
            # print(cook_book)
            nn += 1
            print("Блюдо №", nn)
            dish_name = str_name
            print("Имя блюда:", dish_name)

        elif count == 2:  # Формируем значеия словаря
            recip_len = int(str_name)
        #
        elif count >= 3 and count < recip_len + 3:

            ingr = str_name.strip().split("|")
            for i in ingr:
                i.strip()
                # print(i)
                list_name_temp.append(i)

        # Вычисляем пробелы в рецепте
        elif len(line.strip()) == 0:
            count = 0
            print("Имя блюда:", dish_name)
            cook_book[dish_name] = list_name_temp
            # print(cook_book)
            # print(list_name_temp, type(list_name_temp))
            # print()
            #list_name_temp.clear()
            print(cook_book)

    #print(list_name_temp)

print('----------------')
print(cook_book, type(cook_book))
print('Размер рецепта:', count, "строк")

# cook_book = {}
# list_name_temp = ['Яйцо ', ' 2 ', ' шт', 'Молоко ', ' 100 ', ' мл', 'Помидор ', ' 2 ', ' шт']
# cook_book["Омлет"] = list_name_temp
# print(cook_book)
