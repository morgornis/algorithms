# Проверка корректности кучи - является ли заданный массив корректной кучей (минимум или максимум)

def is_max_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

def test_is_max_heap():
    # Тест 1: Массив, представляющий максимальную кучу
    assert is_max_heap([10, 9, 8, 7, 6, 5]) == True, "Test case 1 failed"

    # Тест 2: Массив, не представляющий максимальную кучу
    assert is_max_heap([10, 9, 8, 7, 12, 5]) == False, "Test case 2 failed"

    # Тест 3: Пустой массив
    assert is_max_heap([]) == True, "Test case 3 failed"

    # Тест 4: Массив с одним элементом
    assert is_max_heap([1]) == True, "Test case 4 failed"

    # Тест 5: Массив с двумя элементами, где корень больше
    assert is_max_heap([2, 1]) == True, "Test case 5 failed"

    # Тест 6: Массив с двумя элементами, где корень меньше
    assert is_max_heap([1, 2]) == False, "Test case 6 failed"

def test_benchmark_is_max_heap(benchmark):
    # Создание большого массива для бенчмарков
    large_heap = list(range(1000000, 0, -1))  # Массив, представляющий максимальную кучу

    def run_heap():
        is_max_heap(large_heap)

    benchmark(run_heap)


# Проверка корректности кучи через обход в ширину

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_max_heap_bfs(root):
    if not root:
        return True
    
    # Очередь для обхода дерева в ширину (BFS)
    queue = [root]
    should_be_leaf = False
    
    while queue:
        current = queue.pop(0)  # Используем pop(0) для извлечения первого элемента
        
        # Проверяем левый потомок
        if current.left:
            if should_be_leaf or current.left.val > current.val:
                return False
            queue.append(current.left)
        else:
            should_be_leaf = True  # Все следующие узлы должны быть листьями
        
        # Проверяем правый потомок
        if current.right:
            if should_be_leaf or current.right.val > current.val:
                return False
            queue.append(current.right)
        else:
            should_be_leaf = True  # Все следующие узлы должны быть листьями
            
    return True

def test_is_max_heap_bfs():
    # Создание тестового дерева, представляющего максимальную кучу
    #      10
    #     /  \
    #    9    8
    #   / \  / \
    #  7  6 5   4
    root = TreeNode(10)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)

    assert is_max_heap_bfs(root) == True, "Test case 1 failed"

    # Тест 2: Дерево, не представляющее максимальную кучу
    root_invalid = TreeNode(10)
    root_invalid.left = TreeNode(12)  # Левый потомок больше
    root_invalid.right = TreeNode(8)
    assert is_max_heap_bfs(root_invalid) == False, "Test case 2 failed"

    # Тест 3: Пустое дерево
    assert is_max_heap_bfs(None) == True, "Test case 3 failed"

    # Тест 4: Дерево с одним узлом
    single_node_tree = TreeNode(1)
    assert is_max_heap_bfs(single_node_tree) == True, "Test case 4 failed"

    # Тест 5: Дерево с двумя элементами, где корень больше
    two_node_tree = TreeNode(2)
    two_node_tree.left = TreeNode(1)
    assert is_max_heap_bfs(two_node_tree) == True, "Test case 5 failed"

    # Тест 6: Дерево с двумя элементами, где корень меньше
    two_node_tree_invalid = TreeNode(1)
    two_node_tree_invalid.left = TreeNode(2)
    assert is_max_heap_bfs(two_node_tree_invalid) == False, "Test case 6 failed"

def test_benchmark_is_max_heap_bfs(benchmark):
    # Создание большого дерева для бенчмарков
    def create_large_max_heap(depth):
        if depth == 0:
            return None
        node = TreeNode(depth)
        node.left = create_large_max_heap(depth - 1)
        node.right = create_large_max_heap(depth - 1)
        return node

    root = create_large_max_heap(10)  # Дерево глубиной 10

    def run():
        is_max_heap_bfs(root)

    benchmark(run)
