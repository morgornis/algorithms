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


# Баланс скобок через префиксные суммы

def can_make_valid_with_deletions(s, k):
    balance = 0
    extra_closed_balance = 0
    
    for char in s:
        if char == '(':
            balance += 1
        else:  # char == ')'
            if balance > 0:
                balance -= 1
            else:
                extra_closed_balance += 1
    
    total_needed = balance + extra_closed_balance
    return total_needed <= k

def test_can_make_valid_with_deletions():
    assert can_make_valid_with_deletions("(()", 1) == True  # Удалив один '(', строка станет валидной
    assert can_make_valid_with_deletions("())", 1) == True  # Удалив один ')', строка станет валидной
    assert can_make_valid_with_deletions("((()))", 0) == True  # Строка уже валидная
    assert can_make_valid_with_deletions(")(", 2) == True  # Удалив оба символа, строка станет валидной
    assert can_make_valid_with_deletions("(((", 3) == True  # Удалив все '(', строка станет валидной
    assert can_make_valid_with_deletions(")))", 3) == True  # Удалив все ')', строка станет валидной
    assert can_make_valid_with_deletions("(()))", 1) == True  # Удалив один ')', строка станет валидной
    assert can_make_valid_with_deletions("())(", 1) == False  # Нельзя сделать валидной с одной удаленной скобкой
    print("Все тесты пройдены!")

def test_benchmark_can_make_valid_with_deletions(benchmark):
    # Бенчмарк функции
    s = "()" * 50 + ")" * 25  # Длинная строка с валидными и лишними закрывающими скобками
    k = 2500
    benchmark(can_make_valid_with_deletions, s, k)
