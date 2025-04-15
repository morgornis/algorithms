# Поиск минимальной глубины бинарного дерева

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def min_depth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is not None and root.right is not None:
        return 1 + min(min_depth(root.left), min_depth(root.right))
    if root.left is not None:
        return 1 + min_depth(root.left)
    if root.right is not None:
        return 1 + min_depth(root.right)

def test_min_depth():
    # Тест 1: Пустое дерево
    assert min_depth(None) == 0

    # Тест 2: Дерево с одним узлом
    root1 = TreeNode(1)
    assert min_depth(root1) == 1

    # Тест 3: Дерево с двумя узлами
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    assert min_depth(root2) == 2

    # Тест 4: Дерево с несколькими узлами
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    assert min_depth(root3) == 2  # Минимальная глубина 2 (1 -> 2)

    # Тест 5: Несимметричное дерево
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    assert min_depth(root4) == 3  # Минимальная глубина 3 (1 -> 2 -> 3)

import random

def generate_balanced_tree(depth):
    if depth < 0:
        return None
    root = TreeNode(random.randint(1, 100))
    root.left = generate_balanced_tree(depth - 1)
    root.right = generate_balanced_tree(depth - 1)
    return root

def test_min_depth_benchmark(benchmark):
    # Генерация сбалансированного дерева глубиной 5
    tree = generate_balanced_tree(5)
    benchmark(min_depth, tree)
