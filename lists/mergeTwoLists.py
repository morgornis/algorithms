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

printList(merged_list)  # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

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
