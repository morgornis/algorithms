# Сумма двух элементов массива

import pytest
import time
import random

def two_sum(data, target):
    cache = {}

    for i in range(len(data)):
        cache[data[i]] = i

    for i in range(len(data)):
        diff = target - data[i]
        if diff in cache and cache[diff] != i:
            return [i, cache[diff]]

    return []

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]  # 2 + 7 = 9
    assert two_sum([3, 2, 4], 6) == [1, 2]       # 2 + 4 = 6
    assert two_sum([3, 3], 6) == [0, 1]          # 3 + 3 = 6
    assert two_sum([5, 1, 5, 3, 7], 10) == [0, 2]   # 5 + 5 = 10
    assert two_sum([], 1) == []                  # Пустой список
    assert two_sum([1, 2, 3], 7) == []            # Нет решения

def test_two_sum_benchmark(benchmark):
    # Генерация тестовых данных
    data = [random.randint(1, 100) for _ in range(10000)]
    target = random.choice(data) + random.choice(data)  # Генерируем целевую сумму

    def run():
        two_sum(data, target)
    
    benchmark(run)
