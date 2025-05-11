# Размен монет

def coin_change(coins, amount, cache=None):
    if cache is None:
        cache = {}
    
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    if amount in cache:
        return cache[amount]

    min_coins = float('inf')

    for coin in coins:
        res = coin_change(coins, amount - coin, cache)
        if res >= 0 and res < min_coins:
            min_coins = res + 1

    cache[amount] = -1 if min_coins == float('inf') else min_coins
    return cache[amount]

# Тесты
def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3, "Тест 1 не пройден"  # 11 = 5 + 5 + 1
    assert coin_change([2], 3) == -1, "Тест 2 не пройден"       # Невозможно сделать 3
    assert coin_change([1], 0) == 0, "Тест 3 не пройден"        # 0 монет
    assert coin_change([1], 2) == 2, "Тест 4 не пройден"        # 2 = 1 + 1
    assert coin_change([1, 2, 3], 4) == 2, "Тест 5 не пройден"  # 4 = 1 + 3 или 2 + 2

    print("Все тесты пройдены успешно!")

def test_benchmark_coin_change(benchmark):
    # Бенчмарк функции
    benchmark(coin_change, [1, 2, 5], 100)  # Измеряем время для большого значения


def coin_change_dp(coins, amount):
    # Создаем массив dp длиной amount + 1 и заполняем его
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Базовый случай: для суммы 0 нужно 0 монет

    # Перебираем все суммы от 1 до amount
    for i in range(1, amount + 1):
        # Проверяем каждую монету
        for coin in coins:
            # Если монета может быть использована для текущей суммы
            if coin <= i:
                # Обновляем минимальное количество монет
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Если сумму нельзя составить, возвращаем -1
    return dp[amount] if dp[amount] != float('inf') else -1

# Тесты
def test_coin_change_dp():
    assert coin_change_dp([1, 2, 5], 11) == 3, "Тест 1 не пройден"  # 11 = 5 + 5 + 1
    assert coin_change_dp([2], 3) == -1, "Тест 2 не пройден"       # Невозможно сделать 3
    assert coin_change_dp([1], 0) == 0, "Тест 3 не пройден"        # 0 монет
    assert coin_change_dp([1], 2) == 2, "Тест 4 не пройден"        # 2 = 1 + 1
    assert coin_change_dp([1, 2, 3], 4) == 2, "Тест 5 не пройден"  # 4 = 1 + 3 или 2 + 2
    assert coin_change_dp([1, 5, 10], 7) == 3, "Тест 6 не пройден"  # 7 = 5 + 1 + 1

    print("Все тесты пройдены успешно!")

def test_benchmark_coin_change_dp(benchmark):
    # Бенчмарк функции
    benchmark(coin_change_dp, [1, 2, 5], 100)  # Измеряем время для большого значения
