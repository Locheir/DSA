# Inserting an element to the end of Linked List : 

class Node : 
    
    def __init__(self, value):    # O(1)
        self.value = value
        self.next = None

class LinkedList :

    def __init__(self):           # O(1)
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):      # O(1)
        new_node = Node(value)
        if self.head is None : 
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node 
        self.length += 1

new_linked_list = LinkedList()

new_linked_list.append(10)
new_linked_list.append(11)
new_linked_list.append(12)

print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)
