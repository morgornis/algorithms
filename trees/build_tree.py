# Восстановление бинарного дерева из массива

import pytest
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def build_tree(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)
    return root

def test_build_tree():
    # Тест 1: Простой случай
    arr = [1, 2, 3, 4, 5]
    root = build_tree(arr)
    assert root.data == 1
    assert root.left.data == 2
    assert root.right.data == 3
    assert root.left.left.data == 4
    assert root.left.right.data == 5

    # Тест 2: Пустой массив
    arr = []
    root = build_tree(arr)
    assert root is None

    # Тест 3: Массив с None
    arr = [1, None, 3]
    root = build_tree(arr)
    assert root.data == 1
    assert root.left is None
    assert root.right.data == 3

    # Тест 4: Полное дерево
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(arr)
    assert root.data == 1
    assert root.left.data == 2
    assert root.right.data == 3
    assert root.left.left.data == 4
    assert root.left.right.data == 5
    assert root.right.left.data == 6
    assert root.right.right.data == 7

def test_build_tree_benchmark(benchmark):
    # Генерация тестовых данных
    data = [random.randint(1, 100) for _ in range(1000)]  # 1000 случайных чисел

    def run():
        build_tree(data)
    
    benchmark(run)
