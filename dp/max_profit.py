# Максимальная выгода

def max_profit(prices):
    if not prices:
        return 0
    
    profit = 0
    min_price = prices[0]
    
    for current_price in prices[1:]:
        profit = max(profit, current_price - min_price)
        min_price = min(current_price, min_price)

    return profit

# Тесты
def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5, "Тест 1 не пройден"
    assert max_profit([7, 6, 4, 3, 1]) == 0, "Тест 2 не пройден"
    assert max_profit([1, 2, 3, 4, 5]) == 4, "Тест 3 не пройден"
    assert max_profit([]) == 0, "Тест 4 не пройден"
    assert max_profit([2, 1]) == 0, "Тест 5 не пройден"
    
    print("Все тесты пройдены успешно!")

def test_benchmark_max_profit(benchmark):
    # Бенчмарк функции
    benchmark(max_profit, [7, 1, 5, 3, 6, 4]) 
