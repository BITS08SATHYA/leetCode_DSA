class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class StackLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def addAtBeginning(self,value):
        node = Node(value)
        if not self.first:
            self.first = node
            self.last = node
        else:
            temp = self.first
            self.first = node
            self.first.next = temp
        self.size += 1
        return self

    def removeFromBeginning(self):
        if not self.first:
            return None
        temp = self.first
        self.first = self.first.next
        self.size -= 1
        if self.size == 0:
            self.last = None
        return temp.value

    def __str__(self):
        temp = self.first
        while temp:
            print(str(temp.value) + " -> ", end="")
            temp = temp.next
        print("None")

a = Node(1)
b = Node(2)
c = Node(3)

stack = StackLinkedList()
stack.addAtBeginning(a)
stack.addAtBeginning(b)
stack.addAtBeginning(c)
stack.__str__()