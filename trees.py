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


# Поиск произведения максимального и минимального элементов из бинарного дерева поиска в виде массива

def max_min_multiplication(data):
    if len(data) < 3:
        return -1

    min_index = 1
    max_index = 2

    # Находим индекс минимального элемента (левые узлы)
    i = 1
    while i < len(data):
        min_index = i
        i = 2 * i + 1  # Переход к следующему левому узлу

    # Находим индекс максимального элемента (правые узлы)
    i = 2
    while i < len(data):
        max_index = i
        i = 2 * i + 2  # Переход к следующему правому узлу

    result = data[min_index] * data[max_index]
    return result

def test_max_min_multiplication():
    # Тест 1: Массив с достаточным количеством элементов
    data1 = [4, 2, 6, 1, 3, 5, 7]
    assert max_min_multiplication(data1) == 7  # 1 * 7 = 7

    # Тест 2: Другой массив, представляющий бинарное дерево поиска
    data2 = [5, 2, 6, 1, 3]
    assert max_min_multiplication(data2) == 6  # 1 * 6 = 6

    # Тест 3: Пустой массив
    data3 = []
    assert max_min_multiplication(data3) == -1  # Ожидаем None для пустого массива

    # Тест 4: Массив с отрицательными числами
    data4 = [-3, -4, -2, -8]
    assert max_min_multiplication(data4) == 16  # -2 * -8 =16

import random

def generate_large_data(size):
    return [random.randint(-10, 10) for _ in range(size)]

def test_max_min_multiplication_benchmark(benchmark):
    # Генерация большого массива
    data = generate_large_data(1000)
    benchmark(max_min_multiplication, data)


# Сравнение двух бинарных деревьев 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def is_same_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.data != b.data:
        return False
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)

def test_is_same_tree():
    # Тест 1: Два одинаковых дерева
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    assert is_same_tree(tree1, tree2) == True, "Test case 1 failed"

    # Тест 2: Два разных дерева
    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)

    assert is_same_tree(tree1, tree3) == False, "Test case 2 failed"

    # Тест 3: Оба дерева пустые
    assert is_same_tree(None, None) == True, "Test case 3 failed"

    # Тест 4: Одно дерево пустое
    assert is_same_tree(tree1, None) == False, "Test case 4 failed"
    assert is_same_tree(None, tree2) == False, "Test case 5 failed"

def test_benchmark_is_same_tree(benchmark):
    # Создание большого дерева для бенчмарков
    def create_large_tree(depth):
        if depth == 0:
            return None
        node = TreeNode(depth)
        node.left = create_large_tree(depth - 1)
        node.right = create_large_tree(depth - 1)
        return node

    tree_a = create_large_tree(10)  # Дерево глубиной 10
    tree_b = create_large_tree(10)  # Другое дерево такой же структуры

    def run():
        is_same_tree(tree_a, tree_b)

    benchmark(run)


# Является ли дерево В поддеревом для А

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def issametree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.data != b.data:
        return False
    return issametree(a.left, b.left) and is_same_tree(a.right, b.right)

def is_subtree(A, B):
    # Пустое дерево B считается поддеревом любого дерева
    if B is None:
        return True
    # Если A пусто, а B нет — не может быть поддеревом
    if A is None:
        return False
    if issametree(A, B):
        return True
    # Рекурсивно проверяем левое и правое поддеревья A
    return is_subtree(A.left, B) or is_subtree(A.right, B)

def test_is_subtree():
    # Тест 1: B является поддеревом A
    A = TreeNode(3)
    A.left = TreeNode(4)
    A.right = TreeNode(5)
    A.left.left = TreeNode(1)
    A.left.right = TreeNode(2)
    A.right.left = TreeNode(0)

    B = TreeNode(4)
    B.left = TreeNode(1)
    B.right = TreeNode(2)

    assert is_subtree(A, B) == True, "Test case 1 failed"

    # Тест 2: B не является поддеревом A
    C = TreeNode(4)
    C.left = TreeNode(1)
    C.right = TreeNode(3)

    assert is_subtree(A, C) == False, "Test case 2 failed"

    # Тест 3: B пустое дерево
    assert is_subtree(A, None) == True, "Test case 3 failed"

    # Тест 4: A пустое дерево
    assert is_subtree(None, B) == False, "Test case 4 failed"

def test_benchmark_is_subtree(benchmark):
    # Создание больших деревьев для бенчмарков
    def create_large_tree(depth):
        if depth == 0:
            return None
        node = TreeNode(depth)
        node.left = create_large_tree(depth - 1)
        node.right = create_large_tree(depth - 1)
        return node

    A = create_large_tree(10)  # Дерево A глубиной 10
    B = create_large_tree(5)   # Дерево B глубиной 5

    def run():
        is_subtree(A, B)

    benchmark(run)


# Зеркальные узлы. Дано бинарное дерево. Необходимо подсчитать количество зеркальных узлов в нем

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def dfs(left, right):
    if left is None or right is None:
        return 0
    count = 0
    # Нашли пару
    if left.data == right.data:
        count = 1
    # Проверяем детей в зеркальном порядке
    count += dfs(left.left, right.right)
    count += dfs(left.right, right.left)
    return count

def count_mirror_twins(root):
    if root is None:
        return 0
    return dfs(root.left, root.right)

def test_count_mirror_twins():
    # Создание тестового дерева
    #      1
    #     / \
    #    2   2
    #   / \ / \
    #  3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    assert count_mirror_twins(root) == 3, "Test case 1 failed"

    # Тест 2: Дерево с одним узлом
    single_node_tree = TreeNode(1)
    assert count_mirror_twins(single_node_tree) == 0, "Test case 2 failed"

    # Тест 3: Пустое дерево
    assert count_mirror_twins(None) == 0, "Test case 3 failed"

    # Тест 4: Дерево без зеркальных пар
    root_no_mirrors = TreeNode(1)
    root_no_mirrors.left = TreeNode(2)
    root_no_mirrors.right = TreeNode(3)
    assert count_mirror_twins(root_no_mirrors) == 0, "Test case 4 failed"

def test_benchmark_count_mirror_twins(benchmark):
    # Создание большого дерева для бенчмарков
    def create_large_mirror_tree(depth):
        if depth == 0:
            return None
        node = TreeNode(depth)
        node.left = create_large_mirror_tree(depth - 1)
        node.right = create_large_mirror_tree(depth - 1)
        return node

    root = create_large_mirror_tree(10)  # Дерево глубиной 10

    def run():
        count_mirror_twins(root)

    benchmark(run)
