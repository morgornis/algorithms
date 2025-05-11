# Поиск компонент связности

def dfs_v(graph, v, visited, component):
    visited[v] = True
    component.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs_v(graph, neighbor, visited, component)

def find_connected_components(graph):
    visited = {i: False for i in range(1, len(graph) + 1)}
    connected_components = []

    for i in range(1, len(graph) + 1):
        if not visited[i]:
            component = []
            dfs_v(graph, i, visited, component)
            connected_components.append(component)

    return connected_components

# Тесты
def test_find_connected_components():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2],
        4: [5],
        5: [4],
        6: []
    }
    expected_result = [[1, 2, 3], [4, 5], [6]]
    assert find_connected_components(graph) == expected_result, "Тест 1 не пройден"

    graph2 = {
        1: [],
        2: [],
        3: [],
        4: []
    }
    expected_result2 = [[1], [2], [3], [4]]
    assert find_connected_components(graph2) == expected_result2, "Тест 2 не пройден"

    print("Все тесты пройдены успешно!")

def test_benchmark_find_connected_components(benchmark):
    # Бенчмарк функции
    graph = {i: [j for j in range(1, 100) if j != i] for i in range(1, 101)}  # Полный граф
    benchmark(find_connected_components, graph)


def dfs_color(graph, v, visited, color):
    visited[v] = color
    for neighbor in graph[v]:
        if visited[neighbor] == 0:
            dfs_color(graph, neighbor, visited, color)

def find_connected_components_color(graph):
    visited = {i: 0 for i in range(1, len(graph) + 1)}
    color = 0

    for node in graph:
        if visited[node] == 0:
            color += 1
            dfs_color(graph, node, visited, color)

    return visited

# Тесты
def test_find_connected_components_color():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2],
        4: [5],
        5: [4],
        6: []
    }
    expected_result = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3}
    assert find_connected_components_color(graph) == expected_result, "Тест 1 не пройден"

    graph2 = {
        1: [],
        2: [],
        3: [],
        4: []
    }
    expected_result2 = {1: 1, 2: 2, 3: 3, 4: 4}
    assert find_connected_components_color(graph2) == expected_result2, "Тест 2 не пройден"

    print("Все тесты пройдены успешно!")

def test_benchmark_find_connected_components_color(benchmark):
    # Бенчмарк функции
    graph = {i: [j for j in range(1, 100) if j != i] for i in range(1, 101)}  # Полный граф
    benchmark(find_connected_components_color, graph)
