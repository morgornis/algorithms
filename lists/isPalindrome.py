from collections import deque

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def printList(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# Является ли слово палиндромом
def isPalindrome_one(s):
    stack = deque()  # Используем deque в качестве стека
    for char in s:
        stack.append(char)  # Добавляем символы в стек

    for char in s:
        if char != stack.pop():  # Сравниваем символ с верхним элементом стека
            return False  # Если не совпадают, возвращаем False

    return True  # Если все символы совпадают, возвращаем True

# Является ли слово палиндромом (два указателя)
def isPalindrome_two(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True  # Если все символы совпадают, возвращаем True

def test_isPalindrome_one():
    assert isPalindrome_one("racecar") == True
    assert isPalindrome_one("hello") == False

def test_isPalindrome_two():
    assert isPalindrome_two("racecar") == True
    assert isPalindrome_two("hello") == False

def test_isPalindrome_one(benchmark):
    s = "racecar"

    def run():
        for _ in range(10):  
            isPalindrome_one(s)
    benchmark(run)

def test_isPalindrome_two(benchmark):
    s = "racecar"

    def run():
        for _ in range(10):  
            isPalindrome_two(s)
    benchmark(run)
