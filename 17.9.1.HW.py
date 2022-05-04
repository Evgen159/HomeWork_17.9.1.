# Программа работает по следующему алгоритму:


# - Преобразование введённой последовательности в список
# - Сортировка списка по возрастанию элементов в нем
# - Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.


import random
import time


# Функция принимает данные с проверкой корректности ввода и выводит сортированный список.
def load_array():
    print('v  Введите последовательность чисел через пробел.  v')
    try:
        # костыль запятая точка для float
        a = list(map(float, input().replace(',', '.').split()))
        end = len(a) - 1
        if end < 1:
            print('Необходимо как минимум два числа. Попробуйте снова.')
            return (load_array())

        # сортируем и выводим список + число
        return sort(a, 0, end), end


    except Exception as ex:
        print('Данные введены не верно.\n', ex,
              '\nЧисла следует вводить через пробел. Для нецелых допускается использовать , и . \nНапример: -968,98 .876 -22 .35 \nПопробуйте снова.')
        print(69 * '*')
        return (load_array())


# Функция ввода числа с контролем.
def load_num():
    print('v  Введите число для сравнения.  v')
    try:
        # костыль запятая точка для float
        n = float(input().replace(',', '.'))
        return n


    except Exception as ex:
        print('Данные введены не верно.\n', ex,
              '\nТребуется одно число. Для нецелых допускается использовать , и . \nНапример: -666,999\nПопробуйте снова.')
        print(69 * '*')
        return (load_num())


# Функция "быстрой" сортировки
def sort(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        sort(array, left, j)
    if right > i:
        sort(array, i, right)
    # array.sort()
    return (array)


# Функция двоичный поиск
# Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if middle and array[middle - 1] < element <= array[middle]:  # если элемент в середине и середина не 0,
        return middle  # требуется вывести именно номер позиции, а не индекс, поэтому +1 от индекса ?
    elif middle and element <= array[middle - 1]:  # если элемент не более эл-та в середине,
        return binary_search(array, element, left, middle - 1)  # рекурсивно ищем в левой половине
    else:
        return binary_search(array, element, middle + 1, right)  # иначе в правой


t0 = time.time()
array, end = load_array()
dt = time.time() - t0
print(dt)
# экспа со временем.
num = load_num()
out = binary_search(array, num, 0, end)

print(69 * '-')
if out:
    print('Номер позиции элемента, который меньше "', num, '", а следующий за ним больше или равен "', num, '":')
    print('"', out, '"')
    array[out - 1] = '*' + str(array[out - 1]) + '*'
else:
    print('Нет элемента, который меньше "', num, '", а следующий за ним больше или равен "', num, '":')

print('Сортированный список (справочная информация):\n', array)
