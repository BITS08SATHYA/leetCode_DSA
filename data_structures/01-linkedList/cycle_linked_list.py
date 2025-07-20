class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def checkLoop(head):
    if not head or not head.next:
        return None
    hare = head
    tortoise = head

    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:
            break
    if hare != tortoise:
        return None

    # find where cycle begins
    pointer = head
    while pointer != tortoise:
        pointer = pointer.next
        tortoise = tortoise.next
    return tortoise


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
# make a loop
six.next = three

head = one
print(checkLoop(head).value)