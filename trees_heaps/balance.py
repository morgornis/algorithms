# Balance factor

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balanceFactor = 0  # Инициализируем баланс-фактор

def calculate_heights_and_balance(node):
    if not node:
        return 0  # Высота пустого дерева равна 0
    
    # Рекурсивно вычисляем высоты левого и правого поддеревьев
    left_height = calculate_heights_and_balance(node.left)
    right_height = calculate_heights_and_balance(node.right)
    
    # Проставляем баланс-фактор текущего узла
    node.balanceFactor = left_height - right_height
    
    # Возвращаем высоту текущего поддерева
    return max(left_height, right_height) + 1

# Тесты
def test_calculate_heights_and_balance():
    # Создаем тестовое дерево
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    calculate_heights_and_balance(root)

    # Проверяем высоты и баланс-факторы
    assert root.balanceFactor == 1, "Root balance factor should be 1"
    assert root.left.balanceFactor == 0, "Left child balance factor should be 0"
    assert root.right.balanceFactor == 0, "Right child balance factor should be 0"
    assert root.left.left.balanceFactor == 0, "Left-left child balance factor should be 0"
    assert root.left.right.balanceFactor == 0, "Left-right child balance factor should be 0"

def test_benchmark_calculate_heights_and_balance(benchmark):
    # Создание большого дерева для бенчмарков
    def create_large_complete_tree(depth):
        if depth == 0:
            return None
        node = TreeNode(depth)
        node.left = create_large_complete_tree(depth - 1)
        node.right = create_large_complete_tree(depth - 1)
        return node

    root = create_large_complete_tree(10)  # Дерево глубиной 10

    # Бенчмарк функции
    benchmark(calculate_heights_and_balance, root)


# Преобразование в зеркальное дерево, т.е. алгоритм перевернет бинарное дерево "вверх ногами" (поменяет местами левые и правые поддеревья каждого узла)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirror_tree(node):
    if node is None:
        return None
    
    # Меняем местами левые и правые поддеревья
    node.left, node.right = node.right, node.left
    
    # Рекурсивно зеркалим поддеревья
    mirror_tree(node.left)
    mirror_tree(node.right)
    
    return node

# Функция для печати дерева в порядке обхода
def print_tree(node):
    if node is None:
        return
    print(node.val, end=' ')
    print_tree(node.left)
    print_tree(node.right)

# Тесты
def test_mirror_tree():
    # Создаем тестовое дерево
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Зеркалим дерево
    mirrored_root = mirror_tree(root)

    # Проверяем структуру зеркального дерева
    assert mirrored_root.val == 1, "Root value should be 1"
    assert mirrored_root.left.val == 3, "Left child should be 3"
    assert mirrored_root.right.val == 2, "Right child should be 2"
    assert mirrored_root.right.left.val == 5, "Right-left child should be 5"
    assert mirrored_root.right.right.val == 4, "Right-right child should be 4"

def test_benchmark_mirror_tree(benchmark):
    # Создание большого дерева для бенчмарков
    def create_large_complete_tree(depth):
        if depth == 0:
            return None
        node = TreeNode(depth)
        node.left = create_large_complete_tree(depth - 1)
        node.right = create_large_complete_tree(depth - 1)
        return node

    root = create_large_complete_tree(10)  # Дерево глубиной 10

    # Бенчмарк функции
    benchmark(mirror_tree, root)
