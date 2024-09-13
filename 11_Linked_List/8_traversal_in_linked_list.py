# Traversal in Linked List

class Node : 

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        tmp_node = self.head
        if self.head:
            result = ''
            while(tmp_node):
                result += str(tmp_node.value)
                if tmp_node.next:
                    result += '->'
                tmp_node = tmp_node.next
            return result
        else:
            return "Linked List is Empty"

    def traversal(self):
        current = self.head 
        while current:
            print(current.value)
            current = current.next
    
l1 = LinkedList()
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)

print(l1)
l1.traversal()