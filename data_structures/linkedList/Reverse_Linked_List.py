class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev.value


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print(reverseLinkedList(head))

