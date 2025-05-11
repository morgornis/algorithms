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
