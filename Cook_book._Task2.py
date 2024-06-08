# Задача №2
# ver. 09.06 00:00

import pprint

cook_book = {}
dish_name = []
count = 0
count_ingr = 0

dishes = []

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        count += 1

        # Считаем длинну строки "l="
        str_name = line.strip()
        l = len(str_name)
        # print(count, str_name)

        if count == 1:  # Определяем ключ словаря dish_name
            # ---- Обнуляем значение, чтобы заново считать новое блюдо
            list_name_temp = []
            ingradients_list = []
            ingredient_dict = {}
            # ----

            # print("Блюдо №", nn)
            dish_name = str_name
            # print("Имя блюда:", dish_name)

        elif count == 2:  # Запоминаем кол-во инградиентов
            recip_len = int(str_name)
        #
        # Формируем список словарей каждого инградиента
        elif count >= 3 and count < recip_len + 3:
            count_ingr += 1
            ingredients = str_name.strip().split("|")
            ingredients_keys = ['ingredient_name', 'quantity', 'measure']
            ingredient_dict = dict(zip(ingredients_keys, ingredients))
            ingradients_list.append(ingredient_dict)
            if count_ingr == recip_len:
                count_ingr = 0  # Обнуляем значение, чтобы заново считать новое блюдо
                cook_book[dish_name] = ingradients_list

        # Вычисляем пробелы в рецепте
        elif len(line.strip()) == 0:
            count = 0  # Обнуляем значение, чтобы заново считать новое блюдо

        else:
            pass

print('----------------')
print(f'cook book = {cook_book.keys()}')
print('--------------', '\n')
# print(cook_book['Омлет'][0])

def get_shop_list_by_dishes(dishes, person_count):
    count_1 = 0
    dic_temp_inradients_ = {}
    dic_temp_amount_ingradients_ = {}
    dic_summ_ingradients = {}
    for dish in dishes:
        #print(cook_book[i])
        list_ingr = cook_book[dish]
        #print(dish, '- Стало')
        for dic_ingradients in list_ingr:
            #Новый словарь для инградиентов и их кол-ва в блюде
            #
            #Создаём едеины измерений
            dic_temp_amount_ingradients_['measure'] = dic_ingradients['measure']
            #
            #Умножаем кол-во инградиентов на кол-во персон
            dic_temp_amount_ingradients_['quantity'] = int(dic_ingradients['quantity'])*person_count
            #print(f'Количество инградиентов: {dic_amount_ingradients}')

            #Новый ключ для кол-ва инградиентов
            new_key = dic_ingradients.get('ingredient_name')
            #print(f'новый ключ: {new_key}')
            #dic_new_[new_key] = {}
            #Создаём словарь инградиентов
            dic_temp_inradients_[new_key] = dic_temp_amount_ingradients_
            print(f'{dic_temp_inradients_}')

            #Создаём общий словарь инградиентов
            #
            #тут пока что то не получается :(
            dic_summ_ingradients.update(dic_temp_inradients_.items())

            #Очищаем временные словари
            dic_temp_amount_ingradients_.clear()
            dic_temp_inradients_.clear()

        print(f'Общий список инградиентов: {dic_summ_ingradients}')

        print('')

    return

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
