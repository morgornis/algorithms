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
