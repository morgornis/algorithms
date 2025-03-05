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

def test_removeElements():
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    new_head = removeElements(head, 6)
    assert new_head.next.next.next.next.value == 5

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
