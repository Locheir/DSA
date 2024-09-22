# Basic Code for Circular Linked List : 

class Node : 

    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList : 

    # def __init__(self, value) :
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# cl1 = CSLinkedList(24)
# print(cl1.head.value)

cl2 = CSLinkedList()
print(cl2.head)