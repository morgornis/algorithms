# Треугольник Паскаля

def pascal_triangle(row, col):
    # Если это вершина треугольника или элемент его стороны
    if col == 0 or row == col:
        return 1
    else:
        return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)

def generate_pascals_triangle(n):
    dp = []
    for row in range(n):
        currentRow = []
        for col in range(row + 1):
            currentRow.append(pascal_triangle(row, col))
        dp.append(currentRow)
    return dp

# Тесты
def test_generate_pascals_triangle():
    result = generate_pascals_triangle(6)
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1]
    ]
    assert result == expected, f"Ожидалось {expected}, но получено {result}"
    print("Все тесты пройдены успешно!")

def test_benchmark_generate_pascals_triangle(benchmark):
    # Бенчмарк функции
    benchmark(generate_pascals_triangle, 6)  # Измеряем время для n = 6


def generate_pascals_triangle_iter(n):
    # Создаем двумерный массив для хранения треугольника Паскаля
    dp = []
    for i in range(n):
        tmp = [1] * (i + 1)  # Заполняем строку единицами
        dp.append(tmp)

    # Заполняем массив значениями
    for row in range(2, n):  # Начинаем с третьей строки (индекс 2)
        for col in range(1, row):  # Начинаем со второго элемента в строке
            dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]

    return dp

# Тесты
def test_generate_pascals_triangle_iter():
    result = generate_pascals_triangle_iter(6)
    expected = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1]
    ]
    assert result == expected, f"Ожидалось {expected}, но получено {result}"
    print("Все тесты пройдены успешно!")

def test_benchmark_generate_pascals_triangle_iter(benchmark):
    # Бенчмарк функции
    benchmark(generate_pascals_triangle_iter, 6)  # Измеряем время для n = 6
