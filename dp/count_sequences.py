# Последовательность без трех единиц подряд

def count_sequences(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    
    dp = [1, 2, 4]  # Начальные значения для n = 0, 1, 2

    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    
    return dp[n]

# Тесты
def test_count_sequences():
    # Проверяем базовые случаи
    assert count_sequences(0) == 1, "count_sequences(0) должно быть 1"
    assert count_sequences(1) == 2, "count_sequences(1) должно быть 2"
    assert count_sequences(2) == 4, "count_sequences(2) должно быть 4"
    
    # Проверяем несколько значений
    assert count_sequences(3) == 7, "count_sequences(3) должно быть 7"
    assert count_sequences(4) == 13, "count_sequences(4) должно быть 13"
    assert count_sequences(5) == 24, "count_sequences(5) должно быть 24"
    assert count_sequences(6) == 44, "count_sequences(6) должно быть 44"

    print("Все тесты пройдены успешно!")

def test_benchmark_count_sequences(benchmark):
    # Бенчмарк функции
    benchmark(count_sequences, 30)  # Измеряем время для n = 30
