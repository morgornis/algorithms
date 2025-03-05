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

# Является ли одна строка исходной для другой (очередь)
def isSubsequence_one(a, b):
    q = deque()
    for el in a:
        q.append(el)
    for el in b:
        if q and q[0] == el:  # Проверяем, совпадает ли первый элемент очереди с текущим элементом b
            q.popleft()  # Удаляем первый элемент из очереди
    return len(q) == 0  # Если очередь пуста, значит a является подпоследовательностью b

# Является ли одна строка исходной для другой (метод двух указателей)
def isSubsequence_two(a, b):
    i, j = 0, 0 
    while i < len(a) and j < len(b):              
        if a[i] == b[j]:
            i += 1 
        j += 1
    return i == len(a)  # Если i достигло длины a, значит a является подпоследовательностью b

def test_isSubsequence_one():
    assert isSubsequence_one("abc", "ahbgdc") == True
    assert isSubsequence_one("axc", "ahbgdc") == False

def test_isSubsequence_two():
    assert isSubsequence_two("abc", "ahbgdc") == True
    assert isSubsequence_two("axc", "ahbgdc") == False

def test_isSubsequence_one(benchmark):
    s = "abc"
    t = "ahbgdc"

    def run():
        for _ in range(10):  
            isSubsequence_one(s, t)
    benchmark(run)

def test_isSubsequence_two(benchmark):
    s = "abc"
    t = "ahbgdc"

    def run():
        for _ in range(10):  
            isSubsequence_two(s, t)
    benchmark(run)
