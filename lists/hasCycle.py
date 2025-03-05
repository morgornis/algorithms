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

def test_hasCycle():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head  # Цикл
    assert hasCycle(head) == True

    head = ListNode(1)
    head.next = ListNode(2)
    assert hasCycle(head) == False

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
