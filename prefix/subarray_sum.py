# Количество непрерывных подмассивов, сумма которых равна k

def subarray_sum(nums, k):
    prefix_sum = 0
    prefix_count = {0: 1}  # Инициализация: префиксная сумма 0 встречается 1 раз
    count = 0

    for num in nums:
        prefix_sum += num
        # Проверяем, есть ли в prefix_count значение prefix_sum - k
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]
        # Обновляем словарь для текущей префиксной суммы
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count

def test_subarray_sum():
    assert subarray_sum([1, 1, 1], 2) == 2  # [1, 1] и [1, 1]
    assert subarray_sum([1, 2, 3], 3) == 2  # [3] и [1, 2]
    assert subarray_sum([5, 1, -1, 2, 3], 5) == 4  # [5] и [2, 3] и их комбинации с [1, -1]
    assert subarray_sum([], 0) == 0  # Пустой массив
    assert subarray_sum([0, 0, 0], 0) == 6  # Все подмассивы равны 0
    print("Все тесты пройдены!")

def test_benchmark_subarray_sum(benchmark):
    # Бенчмарк функции
    nums = [i for i in range(1, 101)]  # Массив от 1 до 10000
    k = 50  # Пример значения k
    benchmark(subarray_sum, nums, k)
