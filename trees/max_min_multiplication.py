# Поиск произведения максимального и минимального элементов из бинарного дерева поиска в виде массива

def max_min_multiplication(data):
    if len(data) < 3:
        return -1

    min_index = 1
    max_index = 2

    # Находим индекс минимального элемента (левые узлы)
    i = 1
    while i < len(data):
        min_index = i
        i = 2 * i + 1  # Переход к следующему левому узлу

    # Находим индекс максимального элемента (правые узлы)
    i = 2
    while i < len(data):
        max_index = i
        i = 2 * i + 2  # Переход к следующему правому узлу

    result = data[min_index] * data[max_index]
    return result

def test_max_min_multiplication():
    # Тест 1: Массив с достаточным количеством элементов
    data1 = [4, 2, 6, 1, 3, 5, 7]
    assert max_min_multiplication(data1) == 7  # 1 * 7 = 7

    # Тест 2: Другой массив, представляющий бинарное дерево поиска
    data2 = [5, 2, 6, 1, 3]
    assert max_min_multiplication(data2) == 6  # 1 * 6 = 6

    # Тест 3: Пустой массив
    data3 = []
    assert max_min_multiplication(data3) == -1  # Ожидаем None для пустого массива

    # Тест 4: Массив с отрицательными числами
    data4 = [-3, -4, -2, -8]
    assert max_min_multiplication(data4) == 16  # -2 * -8 =16

import random

def generate_large_data(size):
    return [random.randint(-10, 10) for _ in range(size)]

def test_max_min_multiplication_benchmark(benchmark):
    # Генерация большого массива
    data = generate_large_data(1000)
    benchmark(max_min_multiplication, data)
