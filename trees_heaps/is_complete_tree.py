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
