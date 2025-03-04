# Списки

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

# Проверить, является ли список циклическим
def hasCycle(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

# Развернуть односвязный список
def reverseLinkedList(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next  # Сохраняем следующий узел
        current.next = prev       # Изменяем указатель текущего узла
        prev = current            # Перемещаем указатель prev на текущий узел
        current = next_node       # Переходим к следующему узлу

    return prev  # new head

# Найти середину списка
def middleNode(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

# Удалить элемент из односвязного списка
def removeElements(head, val):
    dummy = ListNode()  # Создаем "пустой" узел
    dummy.next = head   # Указатель на голову списка
    prev = dummy        # Указатель на предыдущий узел
    cur = head          # Указатель на текущий узел

    while cur is not None:
        if cur.value == val:
            prev.next = cur.next  # Пропускаем узел с нужным значением
        else:
            prev = cur  # Перемещаем указатель prev на текущий узел
        cur = cur.next  # Переходим к следующему узлу

    return dummy.next  # Возвращаем новый список, начиная с первого узла

# Является ли одна строка исходной для другой (очередь)
def isSubsequence_one(a, b):
    q = deque()
    for el in a:
        q.append(el)
    for el in b:
        if q and q[0] == el:  # Проверяем, совпадает ли первый элемент очереди с текущим элементом b
            q.popleft()  # Удаляем первый элемент из очереди
    return len(q) == 0  # Если очередь пуста, значит, a является подпоследовательностью b

# Является ли одна строка исходной для другой (метод двух указателей)
def isSubsequence_two(a, b):
    i, j = 0, 0 
    while i < len(a) and j < len(b):              
        if a[i] == b[j]:
            i += 1 
        j += 1
    return i == len(a)  # Если i достигло длины a, значит, a является подпоследовательностью b

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

# Слияние двух отсортированных списков
def mergeTwoLists(l1, l2):
    # Создаем фиктивный узел для упрощения процесса объединения
    dummy = ListNode()
    cur = dummy  # Указатель на конец нового списка

    # Обходим оба списка, пока не достигнем конца одного из них
    while l1 and l2:
        if l1.value <= l2.value:
            cur.next = ListNode(l1.value)  # Создаем новый узел из значения l1
            l1 = l1.next  # Переходим к следующему узлу в первом списке
        else:
            cur.next = ListNode(l2.value)  # Создаем новый узел из значения l2
            l2 = l2.next  # Переходим к следующему узлу во втором списке
        cur = cur.next  # Перемещаем указатель конца нового списка

    # Если остались узлы в одном из списков, добавляем их
    while l1:
        cur.next = ListNode(l1.value)  # Создаем новый узел из оставшихся значений l1
        l1 = l1.next
        cur = cur.next

    while l2:
        cur.next = ListNode(l2.value)  # Создаем новый узел из оставшихся значений l2
        l2 = l2.next
        cur = cur.next

    return dummy.next  # Возвращаем следующий узел после фиктивного


l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))

merged_list = mergeTwoLists(l1, l2)

#printList(merged_list)  # Вывод: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# Тесты
import pytest
import time
from collections import deque

# Тесты
def test_hasCycle():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head  # Цикл
    assert hasCycle(head) == True

    head = ListNode(1)
    head.next = ListNode(2)
    assert hasCycle(head) == False

def test_reverseLinkedList():
    head = ListNode(1, ListNode(2, ListNode(3)))
    reversed_head = reverseLinkedList(head)
    assert reversed_head.value == 3
    assert reversed_head.next.value == 2
    assert reversed_head.next.next.value == 1
    assert reversed_head.next.next.next is None

def test_middleNode():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert middleNode(head).value == 3

def test_removeElements():
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    new_head = removeElements(head, 6)
    assert new_head.next.next.next.next.value == 5  # 1 -> 2 -> 3 -> 4 -> 5 -> None

def test_isSubsequence_one():
    assert isSubsequence_one("abc", "ahbgdc") == True
    assert isSubsequence_one("axc", "ahbgdc") == False

def test_isSubsequence_two():
    assert isSubsequence_two("abc", "ahbgdc") == True
    assert isSubsequence_two("axc", "ahbgdc") == False

def test_isPalindrome_one():
    assert isPalindrome_one("racecar") == True
    assert isPalindrome_one("hello") == False

def test_isPalindrome_two():
    assert isPalindrome_two("racecar") == True
    assert isPalindrome_two("hello") == False

def test_mergeTwoLists():
    l1 = ListNode(1, ListNode(3, ListNode(5)))
    l2 = ListNode(2, ListNode(4, ListNode(6)))
    merged_head = mergeTwoLists(l1, l2)
    assert merged_head.value == 1
    assert merged_head.next.value == 2
    assert merged_head.next.next.value == 3
    assert merged_head.next.next.next.value == 4
    assert merged_head.next.next.next.next.value == 5
    assert merged_head.next.next.next.next.next.value == 6
    assert merged_head.next.next.next.next.next.next is None

# Бенчмарки
def test_hasCycle(benchmark):
    head = ListNode(1)
    current = head
    for i in range(2, 11):
        current.next = ListNode(i)
        current = current.next
    current.next = head  # Создаем цикл

    def run():
        for i in range(1, 11):
            hasCycle(head)
    benchmark(run)

def test_reverseLinkedList(benchmark):
    head = ListNode(1)
    current = head
    for i in range(2, 11):
        current.next = ListNode(i)
        current = current.next

    def run():
        for _ in range(10):  
            reverseLinkedList(head)
    benchmark(run)

def test_middleNode(benchmark):
    head = ListNode(1)
    current = head
    for i in range(2, 11):
        current.next = ListNode(i)
        current = current.next

    def run():
        for _ in range(10):  
            middleNode(head)
    benchmark(run)

def test_removeElements(benchmark):
    head = ListNode(1)
    current = head
    for i in range(2, 11):
        current.next = ListNode(i)
        current = current.next

    def run():
        for _ in range(10):  
            removeElements(head, 6)
    benchmark(run)

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

def test_mergeTwoLists(benchmark):
    l1 = ListNode(1)
    current = l1
    for i in range(2, 6):
        current.next = ListNode(i)
        current = current.next

    l2 = ListNode(2)
    current = l2
    for i in range(3, 7):
        current.next = ListNode(i)
        current = current.next

    def run():
        for _ in range(10): 
            mergeTwoLists(l1, l2)
    benchmark(run)