# Является ли граф деревом

def is_tree(graph, start):
    visited = []
    queue = [start]
    parent = {start: None}

    while queue:
        vertex = queue.pop(0)
        visited.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = vertex
            else:
                if parent[vertex] != neighbor:
                    return False

    return len(visited) == len(graph)

# Тесты
def test_is_tree():
    graph_tree = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A'],
        'D': ['B'],
        'E': ['B']
    }
    assert is_tree(graph_tree, 'A') == True, "Тест 1 не пройден"

    graph_not_tree = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }
    assert is_tree(graph_not_tree, 'A') == False, "Тест 2 не пройден"

    graph_disconnected = {
        'A': ['B'],
        'B': ['A'],
        'C': []
    }
    assert is_tree(graph_disconnected, 'A') == False, "Тест 3 не пройден"

    print("Все тесты пройдены успешно!")

def test_benchmark_is_tree(benchmark):
    # Бенчмарк функции
    graph = {i: [i + 1] for i in range(1, 100)}  # Линейный граф (дерево)
    graph[99] = [] 
    benchmark(is_tree, graph, 1)
