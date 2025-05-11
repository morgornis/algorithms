# Поиск цикла в графе

def dfs(graph, vertex, parent, visited):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor != parent:
            if neighbor in visited or dfs(graph, neighbor, vertex, visited):
                return True
    return False

def has_cycle(graph):
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            if dfs(graph, vertex, None, visited):
                return True
    return False

# Тесты
def test_has_cycle():
    graph_with_cycle = {
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 1]  # Цикл между 1, 2, 3, 4
    }
    assert has_cycle(graph_with_cycle) == True, "Тест 1 не пройден"

    graph_without_cycle = {
        1: [2],
        2: [1, 3],
        3: [2],
        4: []
    }
    assert has_cycle(graph_without_cycle) == False, "Тест 2 не пройден"

    print("Все тесты пройдены успешно!")

def test_benchmark_has_cycle(benchmark):
    # Бенчмарк функции
    graph = {i: [i + 1] for i in range(1, 100)}  # Линейный граф без цикла
    graph[99] = [1]  # Добавляем цикл
    benchmark(has_cycle, graph)
