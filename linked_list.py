# how to create node
class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
print(a.data)
print(a.next)

a.next = b
b.next = c
print(a.next)
print(int(0x0000022C02436F90))
# empty linked list

class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

L = LinkedList()
print(L)

