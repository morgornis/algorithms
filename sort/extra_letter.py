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
