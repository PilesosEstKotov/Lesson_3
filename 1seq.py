""" Модуль 1 """
num_elements = int(input("Введите количество элементов: "))

elements = []

for i in range(1, num_elements + 1):
    element = int(input(f"Введите {i} элемент: "))
    elements.append(element)

elements.sort()


print(elements)