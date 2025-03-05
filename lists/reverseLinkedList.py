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

def test_reverseLinkedList():
    head = ListNode(1, ListNode(2, ListNode(3)))
    reversed_head = reverseLinkedList(head)
    assert reversed_head.value == 3
    assert reversed_head.next.value == 2
    assert reversed_head.next.next.value == 1
    assert reversed_head.next.next.next is None

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
