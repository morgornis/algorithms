# Объединение K отсорт. массивов в один отсорт. массив. Исп. минкучу для хранения наим. элементов текущих массивов, что позволит извлекать их по очереди, сохраняя порядок

import heapq

def merge_k_sorted_arrays(sorted_arrays):
    # Итоговый массив
    merged_array = []
    # Минимальная куча
    min_heap = []

    # Инициализируем кучу с первым элементом каждого массива
    for i in range(len(sorted_arrays)):
        current_array = sorted_arrays[i]
        # Проверяем, что массив не пустой
        if len(current_array) > 0:
            # (значение, индекс массива, индекс элемента)
            heapq.heappush(min_heap, (current_array[0], i, 0))

    # Пока куча не пуста
    while min_heap:
        # Извлекаем наименьший элемент из кучи
        value, array_idx, element_idx = heapq.heappop(min_heap)
        # Добавляем его в итоговый массив
        merged_array.append(value)

        # Проверяем, есть ли следующий элемент в том же массиве
        if element_idx + 1 < len(sorted_arrays[array_idx]):
            next_element = sorted_arrays[array_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_element, array_idx, element_idx + 1))

    return merged_array

def test_merge_k_sorted_arrays():
    # Тест 1: Слияние нескольких отсортированных массивов
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    assert merge_k_sorted_arrays(arrays) == [1, 1, 2, 3, 4, 4, 5, 6], "Test case 1 failed"

    # Тест 2: Все массивы пустые
    arrays_empty = [[], [], []]
    assert merge_k_sorted_arrays(arrays_empty) == [], "Test case 2 failed"

    # Тест 3: Один массив
    arrays_single = [[1, 2, 3]]
    assert merge_k_sorted_arrays(arrays_single) == [1, 2, 3], "Test case 3 failed"

    # Тест 4: Массивы с одним элементом
    arrays_one_element = [[1], [3], [2]]
    assert merge_k_sorted_arrays(arrays_one_element) == [1, 2, 3], "Test case 4 failed"

    # Тест 5: Массивы с отрицательными числами
    arrays_negatives = [[-1, 3, 5], [-2, -1, 4], [0, 2]]
    assert merge_k_sorted_arrays(arrays_negatives) == [-2, -1, -1, 0, 2, 3, 4, 5], "Test case 5 failed"

    print("Все тесты пройдены успешно!")

def test_benchmark_merge_k_sorted_arrays(benchmark):
    # Тестируем производительность слияния отсортированных массивов
    def run():
        sizes = [10, 100, 1000, 5000]  # Различные размеры массивов
        for size in sizes:
            sorted_arrays = [list(range(i, i + 100)) for i in range(0, size * 100, 100)]  # size массивов по 100 элементов
            merge_k_sorted_arrays(sorted_arrays)

    benchmark(run)
