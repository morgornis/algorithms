# Подсчитать количество последовательностей длины N состоящей из 0 и 1 в которых нет стоящих подряд двух единиц

def b_sequences(n):
    # Определяем базовые случаи
    if n == 0:
        return 1
    elif n == 1:
        return 2
    
    dp = [1, 2]  # Начальные значения последовательности

    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    
    return dp[n]

# Тесты
def test_b_sequences():
    # Проверяем базовые случаи
    assert b_sequences(0) == 1, "b_sequences(0) должно быть 1"
    assert b_sequences(1) == 2, "b_sequences(1) должно быть 2"
    
    # Проверяем несколько значений
    assert b_sequences(2) == 3, "b_sequences(2) должно быть 3"
    assert b_sequences(3) == 5, "b_sequences(3) должно быть 5"
    assert b_sequences(4) == 8, "b_sequences(4) должно быть 8"
    assert b_sequences(5) == 13, "b_sequences(5) должно быть 13"

    print("Все тесты пройдены успешно!")

def test_benchmark_b_sequences(benchmark):
    # Бенчмарк функции
    benchmark(b_sequences, 30)  # Измеряем время для n = 30
