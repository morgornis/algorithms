# Найти корень числа (ближайшее целое)

def binary_search_sqrt(target):
    l, r = 0, target
    while l <= r:
        middle = (l + r) // 2
        middle_squared = middle ** 2
        
        if middle_squared > target:
            r = middle - 1
        elif middle_squared < target:
            l = middle + 1
        else:
            return middle
    return r

import pytest

# Тесты
def test_binary_search_sqrt():
    # Тесты для известных значений
    assert binary_search_sqrt(25) == 5
    assert binary_search_sqrt(10) == 3
    assert binary_search_sqrt(0) == 0
    assert binary_search_sqrt(1) == 1
    assert binary_search_sqrt(2) == 1
    assert binary_search_sqrt(8) == 2
    
    # Тесты для больших значений
    assert binary_search_sqrt(10000) == 100
    assert binary_search_sqrt(999999) == 999

    # Проверка на большие числа
    assert binary_search_sqrt(100000000) == 10000

# Бенчмарки
def test_binary_search_sqrt_benchmark(benchmark):
    target = 1000000

    def run():
        binary_search_sqrt(target)
    benchmark(run)
