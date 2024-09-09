## Creating the Linked List Class : 
#
# creating the linked list with only one node.

class Node : 
    
    def __init__(self, value):   # O(1)
        self.value = value
        self.next = None

class LinkedList :

    def __init__(self, value):   # O(1)
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
new_linked_list = LinkedList(10)

print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)
    