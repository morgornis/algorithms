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


# Наибольшая непрерывная возрастающая последовательность

def findLIS(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    
    dp = [1] * len(nums)  # Инициализируем массив для хранения длин подпоследовательностей

    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1
    
    return max(dp)

# Тесты
def test_findLIS():
    # Проверяем несколько случаев
    assert findLIS([]) == 0, "Должно быть 0 для пустого списка"
    assert findLIS([1]) == 1, "Должно быть 1 для списка из одного элемента"
    assert findLIS([1, 2, 3, 4]) == 4, "Должно быть 4 для возрастающей последовательности"
    assert findLIS([4, 3, 2, 1]) == 1, "Должно быть 1 для убывающей последовательности"
    assert findLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 3, "Должно быть 3 для смешанной последовательности"

    print("Все тесты пройдены успешно!")

def test_benchmark_findLIS(benchmark):
    # Бенчмарк функции
    benchmark(findLIS, [10, 9, 2, 5, 3, 7, 101, 18] * 1000)  # Измеряем время для большого списка


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


# Максимальный палиндром в строке

def longest_palindrome(s):
    current_max_left = 0
    current_max_right = 0

    def expand_around_center(left, right):
        nonlocal current_max_left, current_max_right
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left) > (current_max_right - current_max_left):
                current_max_right = right
                current_max_left = left
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)    # Строка нечетной длины
        expand_around_center(i, i + 1) # Строка четной длины

    return s[current_max_left:current_max_right + 1]

# Тесты
def test_longest_palindrome():
    assert longest_palindrome("babad") in ["bab", "aba"], "Тест 1 не пройден"  # Ожидается "bab" или "aba"
    assert longest_palindrome("cbbd") == "bb", "Тест 2 не пройден"              # Ожидается "bb"
    assert longest_palindrome("a") == "a", "Тест 3 не пройден"                  # Ожидается "a"
    assert longest_palindrome("ac") == "a", "Тест 4 не пройден"                 # Ожидается "a" или "c"
    assert longest_palindrome("racecar") == "racecar", "Тест 5 не пройден"     # Ожидается "racecar"
    
    print("Все тесты пройдены успешно!")

def test_benchmark_longest_palindrome(benchmark):
    # Бенчмарк функции
    benchmark(longest_palindrome, "a" * 100 + "b" + "a" * 100)  # Длинная строка


def longest_palindrome_dp(s):
    n = len(s)
    if n == 0:
        return ""
    
    # Создаем двумерный массив dp
    dp = [[False] * n for _ in range(n)]
    max_length = 1
    start_index = 0

    # Каждая буква сама по себе является палиндромом
    for i in range(n):
        dp[i][i] = True

    # Проверяем подстроки длиной 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start_index = i
            max_length = 2

    # Заполняем таблицу dp
    for length in range(3, n + 1):  # длина подстроки
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start_index = i
                max_length = length

    return s[start_index:start_index + max_length]

# Тесты
def test_longest_palindrome_dp():
    assert longest_palindrome_dp("babad") in ["bab", "aba"], "Тест 1 не пройден"  # Ожидается "bab" или "aba"
    assert longest_palindrome_dp("cbbd") == "bb", "Тест 2 не пройден"              # Ожидается "bb"
    assert longest_palindrome_dp("a") == "a", "Тест 3 не пройден"                  # Ожидается "a"
    assert longest_palindrome_dp("ac") == "a", "Тест 4 не пройден"                 # Ожидается "a" или "c"
    assert longest_palindrome_dp("racecar") == "racecar", "Тест 5 не пройден"     # Ожидается "racecar"
    
    print("Все тесты пройдены успешно!")

def test_benchmark_longest_palindrome_dp(benchmark):
    # Бенчмарк функции
    benchmark(longest_palindrome_dp, "a" * 100 + "b" + "a" * 100)  # Длинная строка
