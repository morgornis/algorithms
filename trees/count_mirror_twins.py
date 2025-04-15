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
