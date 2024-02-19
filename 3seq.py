""" Модуль 3 """

def get_list_from_input(prompt):
    """Получение списка из строки, введенной пользователем."""
    user_input = input(prompt)
    # Превратим введенные значения в список чисел, используя запятую в качестве разделителя
    return [int(item) for item in user_input.split(',')]

# Получаем оба списка от пользователя
list1 = get_list_from_input("Введите элементы 1-го списка: ")
list2 = get_list_from_input("Введите элементы 2-го списка: ")

# Удаляем из первого списка элементы, присутствующие во втором списке
result_list = [item for item in list1 if item not in list2]

# Выводим результат
print("Результат:", ','.join(map(str, result_list)))