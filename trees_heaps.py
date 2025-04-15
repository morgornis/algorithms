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


# Полное бинарное дерево. Является ли данное бинарное дерево полным

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_complete_tree(root):
    if not root:
        return True
    
    queue = [root]
    seen_null = False
    
    while queue:
        node = queue.pop(0)  # Используем pop(0) для извлечения первого элемента
        
        if not node:
            seen_null = True
        else:
            if seen_null:
                return False
            queue.append(node.left)
            queue.append(node.right)
    
    return True

def test_is_complete_tree():
    # Создание тестового дерева, представляющего полное дерево
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root_complete = TreeNode(1)
    root_complete.left = TreeNode(2)
    root_complete.right = TreeNode(3)
    root_complete.left.left = TreeNode(4)
    root_complete.left.right = TreeNode(5)

    assert is_complete_tree(root_complete) == True, "Test case 1 failed"

    # Тест 2: Дерево, не представляющее полное дерево
    root_incomplete = TreeNode(1)
    root_incomplete.left = TreeNode(2)
    root_incomplete.right = TreeNode(3)
    root_incomplete.left.left = TreeNode(4)
    # Пропускаем правый потомок для 2
    root_incomplete.left.right = None
    root_incomplete.right.left = TreeNode(5)  # Добавляем узел, который делает дерево неполным

    assert is_complete_tree(root_incomplete) == False, "Test case 2 failed"

    # Тест 3: Пустое дерево
    assert is_complete_tree(None) == True, "Test case 3 failed"

    # Тест 4: Дерево с одним узлом
    single_node_tree = TreeNode(1)
    assert is_complete_tree(single_node_tree) == True, "Test case 4 failed"

    # Тест 5: Дерево с двумя элементами, где корень имеет только левый потомок
    two_node_tree = TreeNode(1)
    two_node_tree.left = TreeNode(2)
    assert is_complete_tree(two_node_tree) == True, "Test case 5 failed"

def test_benchmark_is_complete_tree(benchmark):
    # Создание большого полного дерева для бенчмарков
    def create_large_complete_tree(depth):
        if depth == 0:
            return None
        node = TreeNode(depth)
        node.left = create_large_complete_tree(depth - 1)
        node.right = create_large_complete_tree(depth - 1)
        return node

    root = create_large_complete_tree(10)  # Дерево глубиной 10

    def run():
        is_complete_tree(root)

    benchmark(run)


# Объединение K отсорт. массивов в один отсорт. массив. Исп. минкучу для хранения наим. элементов текущих массивов, что позволит извлекать их по очереди, сохраняя порядок

import heapq

def merge_k_sorted_arrays(sorted_arrays):
    # Итоговый массив
    merged_array = []
    # Минимальная куча
    min_heap = []

    # Инициализируем кучу с первым элементом каждого массива
    for i in range(len(sorted_arrays)):
        current_array = sorted_arrays[i]
        # Проверяем, что массив не пустой
        if len(current_array) > 0:
            # (значение, индекс массива, индекс элемента)
            heapq.heappush(min_heap, (current_array[0], i, 0))

    # Пока куча не пуста
    while min_heap:
        # Извлекаем наименьший элемент из кучи
        value, array_idx, element_idx = heapq.heappop(min_heap)
        # Добавляем его в итоговый массив
        merged_array.append(value)

        # Проверяем, есть ли следующий элемент в том же массиве
        if element_idx + 1 < len(sorted_arrays[array_idx]):
            next_element = sorted_arrays[array_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_element, array_idx, element_idx + 1))

    return merged_array

def test_merge_k_sorted_arrays():
    # Тест 1: Слияние нескольких отсортированных массивов
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    assert merge_k_sorted_arrays(arrays) == [1, 1, 2, 3, 4, 4, 5, 6], "Test case 1 failed"

    # Тест 2: Все массивы пустые
    arrays_empty = [[], [], []]
    assert merge_k_sorted_arrays(arrays_empty) == [], "Test case 2 failed"

    # Тест 3: Один массив
    arrays_single = [[1, 2, 3]]
    assert merge_k_sorted_arrays(arrays_single) == [1, 2, 3], "Test case 3 failed"

    # Тест 4: Массивы с одним элементом
    arrays_one_element = [[1], [3], [2]]
    assert merge_k_sorted_arrays(arrays_one_element) == [1, 2, 3], "Test case 4 failed"

    # Тест 5: Массивы с отрицательными числами
    arrays_negatives = [[-1, 3, 5], [-2, -1, 4], [0, 2]]
    assert merge_k_sorted_arrays(arrays_negatives) == [-2, -1, -1, 0, 2, 3, 4, 5], "Test case 5 failed"

    print("Все тесты пройдены успешно!")

def test_benchmark_merge_k_sorted_arrays(benchmark):
    # Тестируем производительность слияния отсортированных массивов
    def run():
        sizes = [10, 100, 1000, 5000]  # Различные размеры массивов
        for size in sizes:
            sorted_arrays = [list(range(i, i + 100)) for i in range(0, size * 100, 100)]  # size массивов по 100 элементов
            merge_k_sorted_arrays(sorted_arrays)

    benchmark(run)


# К-ый наименьший/наибольший элемент в BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)
    return root

def inorder_min_iterative(node, k):
    stack = []
    counter = 0
    current = node
    
    while stack or current is not None:
        # Спускаемся влево, добавляя узлы в стек
        while current is not None:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        counter += 1
        
        if counter == k:
            return current.val
        
        current = current.right
    
    return None

# Тесты
def test_inorder_min_iterative():
    arr = [3, 1, 4, None, 2]
    root = build_tree(arr)
    
    assert inorder_min_iterative(root, 1) == 1, "Test case 1 failed"
    assert inorder_min_iterative(root, 2) == 2, "Test case 2 failed"
    assert inorder_min_iterative(root, 3) == 3, "Test case 3 failed"
    assert inorder_min_iterative(root, 4) == 4, "Test case 4 failed"
    print("Все тесты пройдены успешно!")

def test_benchmark_inorder_min_iterative(benchmark):
    # Создание большого дерева для бенчмарков
    def create_large_complete_tree(depth):
        if depth == 0:
            return None
        node = TreeNode(depth)
        node.left = create_large_complete_tree(depth - 1)
        node.right = create_large_complete_tree(depth - 1)
        return node

    root = create_large_complete_tree(10)  # Дерево глубиной 10

    def run():
        for k in range(1, 1025):  # Тестируем для k от 1 до 1024
            inorder_min_iterative(root, k)

    benchmark(run)


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
