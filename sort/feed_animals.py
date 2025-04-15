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
