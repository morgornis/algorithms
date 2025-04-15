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
