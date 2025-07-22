class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    # def __str__(self):
    #     print(self.value)

class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, node):
        # node = Node(value)
        if not self.first:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    def dequeue(self):
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
        values = []
        while temp:
            values.append(str(temp.value))
            # print(str(temp.value))
            temp = temp.next
        return ' -> '.join(values)
a = Node(1)
b = Node(2)
c = Node(3)
queue = QueueLinkedList()
queue.enqueue(a)
queue.enqueue(b)
queue.enqueue(c)
print(queue)
