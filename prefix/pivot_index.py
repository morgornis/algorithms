# Индекс поворота массива

def pivot_index(nums):
    total_sum = sum(nums)  # Вычисляем общую сумму элементов массива
    left_sum = 0

    for i in range(len(nums)):
        # Проверяем, является ли текущий индекс пивотом
        if left_sum == total_sum - left_sum - nums[i]:
            return i  # Возвращаем индекс, если нашли пивот
        # Обновляем left_sum для следующего индекса
        left_sum += nums[i]

    return -1  # Если пивот не найден, возвращаем -1

def test_pivot_index():
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3  # Пивот на индексе 3
    assert pivot_index([1, 2, 3]) == -1  # Нет пивота
    assert pivot_index([2, 1, -1]) == 0  # Пивот на индексе 0
    assert pivot_index([0, 0, 0]) == 0  # Пивот на индексе 0
    assert pivot_index([1, 1, 1, 1, 1]) == 2  # Пивот на индексе 2
    print("Все тесты пройдены!")

def test_benchmark_pivot_index(benchmark):
    # Бенчмарк функции
    nums = list(range(1, 101))
    benchmark(pivot_index, nums)
