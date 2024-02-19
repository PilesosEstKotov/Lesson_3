""" Модуль 2 """


user_input = input("Введите элементы списка через запятую, точку с запятой или слэш: ")


if ',' in user_input:
    delimiter = ','
elif ';' in user_input:
    delimiter = ';'
elif '/' in user_input:
    delimiter = '/'
else:
    print("Неверный формат ввода")
    exit()


elements_list = user_input.split(delimiter)
elements_list = [int(elem) for elem in elements_list]


unique_elements = []


for elem in elements_list:
    if elements_list.count(elem) == 1:
        unique_elements.append(elem)


print("Результат:", ', '.join(map(str, unique_elements)))