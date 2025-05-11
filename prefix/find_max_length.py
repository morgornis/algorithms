# Максимальная длина подмассива с равным количеством нулей и единиц

def find_max_length(nums):
    prefix_sum = 0
    max_len = 0
    index_map = {0: -1}  # Инициализация: сумма 0 встречается на позиции -1

    for i in range(len(nums)):
        num = nums[i]
        # Заменяем 0 на -1, 1 оставляем как +1
        prefix_sum += -1 if num == 0 else 1
        
        if prefix_sum in index_map:
            # Если сумма уже встречалась, обновляем max_len
            max_len = max(max_len, i - index_map[prefix_sum])
        else:
            # Иначе сохраняем первую позицию для этой суммы
            index_map[prefix_sum] = i
            
    return max_len

def test_find_max_length():
    assert find_max_length([0, 1]) == 2  # [0, 1]
    assert find_max_length([0, 1, 0]) == 2  # [0, 1] или [1, 0]
    assert find_max_length([0, 0, 1, 0, 1, 1]) == 6  # Полный массив
    assert find_max_length([1, 1, 0, 0, 1, 1]) == 4  # 4
    assert find_max_length([0, 0, 0, 0]) == 0  # Нет 1
    assert find_max_length([1, 1, 1, 1]) == 0  # Нет 0
    print("Все тесты пройдены!")

def test_benchmark_find_max_length(benchmark):
    # Бенчмарк функции
    nums = [0, 1] * 50
    benchmark(find_max_length, nums)
