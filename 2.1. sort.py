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


# Накормить животных

import pytest
import time
import random

def feed_animals(animals, food):
    if len(animals) == 0 or len(food) == 0:
        return 0

    animals.sort()  # Сортируем животных
    food.sort()     # Сортируем еду

    count = 0
    for f in food:
        if f >= animals[count]:
            count += 1

        if count == len(animals):
            break

    return count

def test_feed_animals():
    assert feed_animals([1, 2, 3], [2, 3, 4]) == 3  # Все животные накормлены
    assert feed_animals([1, 2, 3], [1, 1, 1]) == 1  # Только одно животное накормлено
    assert feed_animals([], [1, 2, 3]) == 0         # Нет животных
    assert feed_animals([1, 2, 3], []) == 0          # Нет еды
    assert feed_animals([5, 6], [1, 2, 3, 4]) == 0  # Невозможно накормить
    assert feed_animals([1, 2], [2, 3]) == 2         # Все животные накормлены

def test_feed_animals_benchmark(benchmark):
    # Генерация тестовых данных
    animals = [random.randint(1, 100) for _ in range(1000)]
    food = [random.randint(1, 100) for _ in range(1000)]

    def run():
        feed_animals(animals, food)
    
    benchmark(run)


# Найти разницу между двух строк

import pytest
import time
import random
import string

def extra_letter(a, b):
    hash_map_a = {}
    
    # Заполняем хеш-таблицу для строки a
    for char in a:
        hash_map_a[char] = hash_map_a.get(char, 0) + 1

    # Проверяем строку b
    for char in b:
        if char in hash_map_a:
            hash_map_a[char] -= 1
            # Если счетчик становится 0, удаляем элемент
            if hash_map_a[char] == 0:
                del hash_map_a[char]
        else:
            # Если буквы нет в a, значит это лишняя буква
            return char

    return ""

def test_extra_letter():
    assert extra_letter("abcd", "abcde") == "e"  # Лишняя буква 'e'
    assert extra_letter("a", "aa") == "a"         # Лишняя буква 'a'
    assert extra_letter("xyz", "xyza") == "a"     # Лишняя буква 'a'
    assert extra_letter("hello", "helloo") == "o" # Лишняя буква 'o'
    assert extra_letter("", "a") == "a"           # Лишняя буква 'a'
    assert extra_letter("abc", "abc") == ""        # Нет лишней буквы

def test_extra_letter_benchmark(benchmark):
    # Генерация тестовых данных
    a = ''.join(random.choices(string.ascii_lowercase, k=1000))
    b = a + random.choice(string.ascii_lowercase)  # Добавляем одну лишнюю букву

    def run():
        extra_letter(a, b)
    
    benchmark(run)


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


# Массив анаграмм

import pytest
import random
import string

def group_anagrams(strs):
    anagram_map = {}
    
    for s in strs:
        # Сортируем строку и используем ее как ключ
        sorted_str = ''.join(sorted(s))
        if sorted_str not in anagram_map:
            anagram_map[sorted_str] = []
        anagram_map[sorted_str].append(s)
    
    # Возвращаем все группы анаграмм
    return list(anagram_map.values())

def test_group_anagrams():
    assert sorted(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert sorted(group_anagrams(["won", "now", "aaa", "ooo", "ooo"])) == sorted([["aaa"], ["ooo", "ooo"], ["won", "now"]])
    assert sorted(group_anagrams([""])) == sorted([[""]])  # Пустая строка
    assert sorted(group_anagrams(["a"])) == sorted([["a"]])  # Одна буква
    assert sorted(group_anagrams(["abc", "cba", "bca", "xyz"])) == sorted([["abc", "bca", "cba"], ["xyz"]])  # Разные анаграммы

def test_group_anagrams_benchmark(benchmark):
    # Генерация тестовых данных
    data = [''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5))) for _ in range(1000)]
    
    def run():
        group_anagrams(data)
    
    benchmark(run)

