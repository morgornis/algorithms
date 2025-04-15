# Сортировка Шелла

import pytest
import random

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Используем целочисленное деление

    while gap > 0:
        for current_position in range(gap, n):
            m_gap = current_position
            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                arr[m_gap], arr[m_gap - gap] = arr[m_gap - gap], arr[m_gap]
                m_gap -= gap
        gap //= 2  # Обновляем значение gap

    return arr

def test_shell_sort():
    assert shell_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert shell_sort([3, 7, 2, 5, 1]) == [1, 2, 3, 5, 7]
    assert shell_sort([1]) == [1]  # Один элемент
    assert shell_sort([]) == []     # Пустой список
    assert shell_sort([4, 3, 2, 1]) == [1, 2, 3, 4]  # Обратный порядок

def test_shell_sort_benchmark(benchmark):
    # Генерация тестовых данных
    data = [random.randint(1, 1000) for _ in range(1000)]  # 1000 случайных чисел

    def run():
        shell_sort(data.copy())  # Используем copy, чтобы не изменять оригинальный список
    
    benchmark(run)
