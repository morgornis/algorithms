# Баланс скобок через префиксные суммы

def can_make_valid_with_deletions(s, k):
    balance = 0
    extra_closed_balance = 0
    
    for char in s:
        if char == '(':
            balance += 1
        else:  # char == ')'
            if balance > 0:
                balance -= 1
            else:
                extra_closed_balance += 1
    
    total_needed = balance + extra_closed_balance
    return total_needed <= k

def test_can_make_valid_with_deletions():
    assert can_make_valid_with_deletions("(()", 1) == True  # Удалив один '(', строка станет валидной
    assert can_make_valid_with_deletions("())", 1) == True  # Удалив один ')', строка станет валидной
    assert can_make_valid_with_deletions("((()))", 0) == True  # Строка уже валидная
    assert can_make_valid_with_deletions(")(", 2) == True  # Удалив оба символа, строка станет валидной
    assert can_make_valid_with_deletions("(((", 3) == True  # Удалив все '(', строка станет валидной
    assert can_make_valid_with_deletions(")))", 3) == True  # Удалив все ')', строка станет валидной
    assert can_make_valid_with_deletions("(()))", 1) == True  # Удалив один ')', строка станет валидной
    assert can_make_valid_with_deletions("())(", 1) == False  # Нельзя сделать валидной с одной удаленной скобкой
    print("Все тесты пройдены!")

def test_benchmark_can_make_valid_with_deletions(benchmark):
    # Бенчмарк функции
    s = "()" * 50 + ")" * 25  # Длинная строка с валидными и лишними закрывающими скобками
    k = 2500
    benchmark(can_make_valid_with_deletions, s, k)
