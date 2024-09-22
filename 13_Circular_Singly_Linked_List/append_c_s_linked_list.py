# Appending in a circular singly linked list : 

class Node : 

    def __init__(self, value) :
        self.value = value
        self.next = None

class CSLinkedList : 

    def __init__(self) :
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head :
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        else :
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        self.length += 1

csll1 = CSLinkedList()
csll1.append(10)
csll1.append(20)

print(csll1.head.value)
print(csll1.tail.value)
print(csll1.tail.next.value)