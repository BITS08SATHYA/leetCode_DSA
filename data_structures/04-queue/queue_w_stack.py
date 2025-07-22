class MyQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, val):
        self.inStack.append(val)

    def pop(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        return len(self.inStack) == 0 and len(self.outStack) == 0

    def __str__(self):
        out_values = list(reversed(self.outStack))
        in_values = self.inStack
        all_values = out_values + in_values
        return '-> '.join(map(str, all_values))

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q)
q.pop()
print(q)