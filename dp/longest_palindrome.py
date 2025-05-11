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
