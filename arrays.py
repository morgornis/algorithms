# Массивы

# Найти два числа в отсорт по возр массиве, кот. в сумме дают target, и вернуть их индексы
def two_sum (nums, target):
    left = 0
    right = len(nums)-1

    while left<right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left, right]
        elif sum < target: left+=1
        else: right -= 1

    return [left, right]

print(two_sum([3,8,9,11,16,18,19,21],25))

# Развернуть массив за лин. время без аллокации памяти
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

print(reverse_array([3,8,6,9,9,8,6]))

# Развернуть часть массива за лин. время без доп. аллокаций
def reverse_array_part(arr, k):
    def reverse_arr(arr, left, right):
        while left<right:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    
    n = len(arr)
    reverse_arr(arr, 0, n-1)
    reverse_arr(arr, 0, abs(k)-1)
    reverse_arr(arr, abs(k), n-1)

    return arr

print(reverse_array_part([1, 2, 3, 4, 5, 6, 7],3))

# Слияние двух отсортированных массивов
def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    # Если в каком-то из массивов остались элементы, добавляем их в конец слияния
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    
    return merged_array

print(merge_sorted_arrays([3,8,10,11],[1,7,9]))

# Слияние двух отсортированных массивов без дополнительных аллокаций
def merge(arr1, arr2):
    pointer1 = len(arr1) - len(arr2) - 1
    pointer2 = len(arr2) - 1
    pointer3 = len(arr1) - 1

    while pointer2 >= 0:
        if pointer1 >= 0 and arr1[pointer1] > arr2[pointer2]:
            arr1[pointer3] = arr1[pointer1]
            pointer1 -= 1
        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -= 1
        pointer3 -= 1

    return arr1

print(merge([3,8,10,11],[1,7,9]))

# Сортировка массива из 0 и 1
def sort_binary_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            # Если arr[left] == 1 и arr[right] == 0, меняем их местами
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    return arr

print(sort_binary_array([0,1,1,0,1,0,1,0]))

# Задача флага Нидерладндов: отсорт. массив из 0,1,2 за линейное время
def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

print(sort_colors([2, 0, 2, 1, 1, 0]))

# Передвинуть четные числа вперед в неотсорт. масиве
def even_first(arr):
    even_index = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[even_index], arr[i] = arr[i], arr[even_index]
            even_index += 1
            
    return arr

print(even_first([3, 2, 4, 1, 11, 8, 9]))

# Нули в конец
def zero_end(arr):
    left = 0
    right = 0

    while right < len(arr):
        if arr[right] == 0:
            right += 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    
    return arr

print(zero_end([0, 0, 1, 0, 3, 12]))


import pytest
import time

# Тесты

def test_two_sum():
    assert two_sum([3, 8, 9, 11, 16, 18, 19, 21], 25) == [2, 4]
    assert two_sum([1, 2, 3, 4, 5], 5) == [0, 3]

def test_reverse_array():
    assert reverse_array([3, 8, 6, 9, 9, 8, 6]) == [6, 8, 9, 9, 6, 8, 3]

def test_reverse_array_part():
    assert reverse_array_part([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

def test_merge_sorted_arrays():
    assert merge_sorted_arrays([3, 8, 10, 11], [1, 7, 9]) == [1, 3, 7, 8, 9, 10, 11]

def test_merge():
    arr1 = [3, 8, 10, 11, 0, 0, 0]
    arr2 = [1, 7, 9]
    assert merge(arr1, arr2) == [1, 3, 7, 8, 9, 10, 11]

def test_sort_binary_array():
    assert sort_binary_array([0, 1, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]

def test_sort_colors():
    assert sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]

def test_even_first():
    assert even_first([3, 2, 4, 1, 11, 8, 9]) == [2, 4, 8, 1, 11, 3, 9]

def test_zero_end():
    assert zero_end([0, 0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0, 0]

# Бенчмарки
def benchmark(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

def test_benchmarks():
    assert benchmark(two_sum, [3, 8, 9, 11, 16, 18, 19, 21], 25) < 0.001
    assert benchmark(reverse_array, [3, 8, 6, 9, 9, 8, 6]) < 0.001
    assert benchmark(reverse_array_part, [1, 2, 3, 4, 5, 6, 7], 3) < 0.001
    assert benchmark(merge_sorted_arrays, [3, 8, 10, 11], [1, 7, 9]) < 0.001
    assert benchmark(merge, [3, 8, 10, 11, 0, 0, 0], [1, 7, 9]) < 0.001
    assert benchmark(sort_binary_array, [0, 1, 1, 0, 1, 0, 1, 0]) < 0.001
    assert benchmark(sort_colors, [2, 0, 2, 1, 1, 0]) < 0.001
    assert benchmark(even_first, [3, 2, 4, 1, 11, 8, 9]) < 0.001
    assert benchmark(zero_end, [0, 0, 1, 0, 3, 12]) < 0.001

test_benchmarks()
