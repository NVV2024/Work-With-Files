# Задача №1
#ver. 08.06 2:11

import pprint

cook_book = {}
dish_name = []
count = 0
count_ingr = 0

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        count += 1

        # Считаем длинну строки "l="
        str_name = line.strip()
        l = len(str_name)
        #print(count, str_name)

        if count == 1:  # Определяем ключ словаря dish_name
            # ---- Обнуляем значение, чтобы заново считать новое блюдо
            list_name_temp = []
            ingradients_list = []
            ingredient_dict = {}
            #----

            #print("Блюдо №", nn)
            dish_name = str_name
            #print("Имя блюда:", dish_name)

        elif count == 2:  # Запоминаем кол-во инградиентов
            recip_len = int(str_name)
        #
        #Формируем список словарей каждого инградиента
        elif count >= 3 and count < recip_len + 3:
            count_ingr += 1
            ingredients = str_name.strip().split("|")
            ingredients_keys = ['ingredient_name', 'quantity', 'measure']
            ingredient_dict = dict(zip(ingredients_keys, ingredients))
            ingradients_list.append(ingredient_dict)
            if count_ingr == recip_len:
                count_ingr = 0    #Обнуляем значение, чтобы заново считать новое блюдо
                cook_book[dish_name] = ingradients_list

        # Вычисляем пробелы в рецепте
        elif len(line.strip()) == 0:
            count = 0    #Обнуляем значение, чтобы заново считать новое блюдо

        else:
            pass

#print('----------------')
print(f'cook book = {cook_book}')
#print('Размер рецепта:', count, "строк")

# cook_book = {}
# list_name_temp = ['Яйцо ', ' 2 ', ' шт', 'Молоко ', ' 100 ', ' мл', 'Помидор ', ' 2 ', ' шт']
# cook_book["Омлет"] = list_name_temp
# print(cook_book)
