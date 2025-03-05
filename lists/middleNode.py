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

# Найти середину списка
def middleNode(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def test_middleNode():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert middleNode(head).value == 3

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
