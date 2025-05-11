# Максимальная сумма подмассива

def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None

    current_sum = sum(arr[:k])  # Сумма первых k элементов
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]  # Сдвигаем окно
        max_sum = max(max_sum, current_sum)

    return max_sum

def test_max_subarray_sum():
    assert max_subarray_sum([1, 2, 3, 4, 5], 2) == 9  # 4 + 5
    assert max_subarray_sum([1, 2, 3, 4, 5], 3) == 12  # 3 + 4 + 5
    assert max_subarray_sum([5, 1, 3, 2, 8], 2) == 10  # 2 + 8
    assert max_subarray_sum([1, 2, 3], 5) is None  # Длина массива меньше k
    assert max_subarray_sum([], 1) is None  # Пустой массив
    print("Все тесты пройдены!")

def test_benchmark_max_subarray_sum(benchmark):
    # Бенчмарк функции
    arr = [i for i in range(1, 101)]
    k = 10
    benchmark(max_subarray_sum, arr, k)
