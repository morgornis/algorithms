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
