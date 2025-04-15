# Симметричное бинарное дерево. На вход функции подается бинарное дерево. Необходимо понять, является ли это дерево симметричным.
# BFS (Breadth-First Search)

import pytest
import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if root is None:
        return True

    queue = [root]
    while queue:
        queue_len = len(queue)
        for i in range(queue_len):
            # Симметричные узлы
            if queue[i] is None and queue[queue_len - i - 1] is None:
                continue
            if queue[i] is None or queue[queue_len - i - 1] is None:
                return False
            if queue[i].data != queue[queue_len - i - 1].data:
                return False
            
            # Добавляем дочерние узлы в очередь
            queue.append(queue[i].left)
            queue.append(queue[i].right)
        
        # Удаляем обработанные узлы из очереди
        queue = queue[queue_len:]

    return True

def test_is_symmetric():
    # Тест 1: Симметричное дерево
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    assert is_symmetric(root1) == True

    # Тест 2: Несимметричное дерево
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)
    assert is_symmetric(root2) == False

    # Тест 3: Пустое дерево
    assert is_symmetric(None) == True

    # Тест 4: Дерево с одним узлом
    root3 = TreeNode(1)
    assert is_symmetric(root3) == True

    # Тест 5: Дерево с двумя узлами
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(2)
    assert is_symmetric(root4) == True

import random

def generate_balanced_tree(depth):
    if depth < 0:
        return None
    root = TreeNode(random.randint(1, 100))
    root.left = generate_balanced_tree(depth - 1)
    root.right = generate_balanced_tree(depth - 1)
    return root

def test_is_symmetric_benchmark(benchmark):
    # Генерация сбалансированного дерева глубиной 5
    tree = generate_balanced_tree(5)
    benchmark(is_symmetric, tree)

# DFS (Depth-First Search)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def dept_search(root, res):
    if root is None:
        return res
    dept_search(root.left, res)
    res.append(root.data)
    dept_search(root.right, res)
    return res

def is_symmetric_dfs(root):
    if root is None:
        return True
    data = []
    data = dept_search(root, data)
    j = len(data) - 1
    for i in range(len(data) // 2):
        if data[i] != data[j]:
            return False
        j -= 1
    return True

def test_is_symmetric_dfs():
    # Тест 1: Симметричное дерево
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    assert is_symmetric_dfs(root1) == True

    # Тест 2: Несимметричное дерево
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)
    assert is_symmetric_dfs(root2) == False

    # Тест 3: Пустое дерево
    assert is_symmetric_dfs(None) == True

    # Тест 4: Дерево с одним узлом
    root3 = TreeNode(1)
    assert is_symmetric_dfs(root3) == True

    # Тест 5: Дерево с двумя узлами
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(2)
    assert is_symmetric_dfs(root4) == True

import random

def generate_balanced_tree(depth):
    if depth < 0:
        return None
    root = TreeNode(random.randint(1, 100))
    root.left = generate_balanced_tree(depth - 1)
    root.right = generate_balanced_tree(depth - 1)
    return root

def test_is_symmetric_dfs_benchmark(benchmark):
    # Генерация сбалансированного дерева глубиной 5
    tree = generate_balanced_tree(5)
    benchmark(is_symmetric_dfs, tree)
