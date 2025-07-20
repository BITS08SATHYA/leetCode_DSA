class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def linkNodes(node1, node2):
    node1.next = node2
    node2.prev = node1

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.next = None
        node.prev = None

    def inserB(self, nodePosition, nodeInsert):
        if self.head == nodeInsert and self.tail == nodeInsert:
            return
        self.remove(nodeInsert)

        nodeInsert.prev = nodePosition.prev
        nodeInsert.next = nodePosition

        if nodePosition == self.head:
            self.head = nodeInsert
        else:
            nodePosition.prev.next = nodeInsert
        nodePosition.prev = nodeInsert

    def allNodesValueRemove(self, value):
        curr = self.head
        while curr:
            temp = curr
            curr = curr.next
            if temp.value == value:
                self.remove(temp)

    def __str__(self):
        curr = self.head
        while curr:
            print(curr.value, end=" <-> " if curr.next else "")
            curr = curr.next
        print()


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Manually link nodes
linkNodes(a, b)
linkNodes(b, c)
linkNodes(c, d)

# Create DLL and assign head/tail
dll = DoublyLinkedList()
dll.head = a
dll.tail = d

dll.remove(d)
dll.__str__()
