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


# Алгоритм Дейкстры. Поиск кратчайшего пути

import heapq

def dijkstra(graph, start):
    # Создаем структуру данных для хранения кратчайших расстояний
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Расстояние до стартовой вершины 0
    
    # Массив для хранения вершин и их расстояний
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Обрабатываем только если текущее расстояние меньше ранее записанного
        if current_distance > distances[current_vertex]:
            continue
        
        # Обновляем расстояния до соседей
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Если нашли более короткий путь
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Тесты
def test_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    assert dijkstra(graph, 'A') == {'A': 0, 'B': 1, 'C': 3, 'D': 4}, "Тест 1 не пройден"
    assert dijkstra(graph, 'B') == {'B': 0, 'A': 1, 'C': 2, 'D': 3}, "Тест 2 не пройден"
    
    print("Все тесты пройдены успешно!")

def test_benchmark_dijkstra(benchmark):
    # Бенчмарк функции
    graph = {str(i): {str(j): j for j in range(1, 100) if j != i} for i in range(1, 100)}  # Большой граф
    benchmark(dijkstra, graph, '1')


# Проверка на двудольность

from collections import deque

def is_bipartite(graph):
    n = len(graph)
    colors = [0] * n  # Массив для хранения цветов вершин (0 - не раскрашена, 1 - первый цвет, -1 - второй цвет)

    def bfs(start):
        queue = deque([start])  # Очередь для BFS
        colors[start] = 1  # Красим начальную вершину в первый цвет
        
        while queue:
            node = queue.popleft()  # Извлекаем текущую вершину
            
            for neighbor in graph[node]:
                if colors[neighbor] == 0:  # Если сосед ещё не раскрашен
                    colors[neighbor] = -colors[node]  # Красим в противоположный цвет
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:  # Если сосед имеет тот же цвет
                    return False  # Граф не двудольный
        return True

    for i in range(n):
        if colors[i] == 0:  # Если вершина ещё не посещена
            if not bfs(i):  # Запускаем BFS и проверяем
                return False

    return True

# Тесты
def test_is_bipartite():
    graph1 = [
        [1, 3],
        [0, 2],
        [1, 3],
        [0, 2]
    ]
    assert is_bipartite(graph1) == True, "Тест 1 не пройден"

    graph2 = [
        [1, 2, 3],
        [0, 3],
        [0, 3],
        [0, 1, 2]
    ]
    assert is_bipartite(graph2) == False, "Тест 2 не пройден"

    graph3 = [
        [1],
        [0, 2],
        [1, 3],
        [2]
    ]
    assert is_bipartite(graph3) == True, "Тест 3 не пройден"

    print("Все тесты пройдены успешно!")

# Бенчмаркинг
import time

def test_benchmark_is_bipartite(benchmark):
    # Создаем большой двудольный граф
    n = 100
    graph = [[] for _ in range(n)]
    for i in range(0, n, 2):
        if i + 1 < n:
            graph[i].append(i + 1)
            graph[i + 1].append(i)

    benchmark(is_bipartite, graph)


def is_bipartite_dfs(graph):
    n = len(graph)
    colors = [0] * n  # Массив для хранения цветов вершин

    def dfs(node, c):
        colors[node] = c  # Красим текущую вершину
        for neighbor in graph[node]:
            if colors[neighbor] == 0:  # Если сосед ещё не раскрашен
                if not dfs(neighbor, -c):  # Красим в противоположный цвет
                    return False
            elif colors[neighbor] == colors[node]:  # Если сосед уже раскрашен в тот же цвет
                return False
        return True

    for i in range(n):
        if colors[i] == 0:  # Если вершина ещё не была посещена
            if not dfs(i, 1):  # Запускаем DFS, начиная с текущей вершины
                return False

    return True

# Тесты
def test_is_bipartite_dfs():
    graph1 = [
        [1, 3],
        [0, 2],
        [1, 3],
        [0, 2]
    ]
    assert is_bipartite_dfs(graph1) == True, "Тест 1 не пройден"

    graph2 = [
        [1, 2, 3],
        [0, 3],
        [0, 3],
        [0, 1, 2]
    ]
    assert is_bipartite_dfs(graph2) == False, "Тест 2 не пройден"

    graph3 = [
        [1],
        [0, 2],
        [1, 3],
        [2]
    ]
    assert is_bipartite_dfs(graph3) == True, "Тест 3 не пройден"

    print("Все тесты пройдены успешно!")

def test_benchmark_is_bipartite_dfs(benchmark):
    # Создаем большой двудольный граф
    n = 1000
    graph = [[] for _ in range(n)]
    for i in range(0, n, 2):
        if i + 1 < n:
            graph[i].append(i + 1)
            graph[i + 1].append(i)

    benchmark(is_bipartite_dfs, graph)
