# Как быстро можно сделать N копий документа, используя два ксерокса, каждый копирует со своей скоростью (x и y минут)?

def copy_time(n, x, y):
    l = 0
    r = (n - 1) * max(x, y)

    while l + 1 < r:
        mid = (l + r) // 2
        if mid // x + mid // y < n - 1:
            l = mid
        else:
            r = mid

    return r + min(x, y)

import pytest

# Тесты
def test_copy_time():
    # Тесты для известных значений
    assert copy_time(3, 2, 3) == 5  # Пример: n=3, x=2, y=3
    assert copy_time(5, 1, 2) == 4  # Пример: n=5, x=1, y=2
    assert copy_time(10, 1, 1) == 6  # Пример: n=10, x=1, y=1
    assert copy_time(4, 2, 2) == 6  # Пример: n=4, x=2, y=2
    assert copy_time(1, 1, 1) == 1  # Пример: n=1, x=1, y=1

# Бенчмарки
def test_copy_time_benchmark(benchmark):
    target_n = 1000
    target_x = 1
    target_y = 2

    def run():
        copy_time(target_n, target_x, target_y)
    
    benchmark(run)
