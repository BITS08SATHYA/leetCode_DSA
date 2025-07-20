class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addAtTail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return self

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return "->".join(result)


def add2Numbers(l1, l2):
    carryForward = 0
    results = LinkedList()
    while l1 or l2 or carryForward:
        l1Value = l1.value if l1 else 0
        l2Value = l2.value if l2 else 0
        sum = (l1Value + l2Value + carryForward)
        nodeValueInResult = sum % 10
        results.addAtTail(nodeValueInResult)
        carryForward = sum // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return results


l1 = LinkedList()
l2 = LinkedList()
l1.addAtTail(8)
l1.addAtTail(2)
l1.addAtTail(6)

l2.addAtTail(7)
l2.addAtTail(6)
l2.addAtTail(5)
# l1 = [6,2,8]
# l2 = [5,6,7]
print(add2Numbers(l1.head, l2.head))

