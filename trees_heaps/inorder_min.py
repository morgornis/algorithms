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
