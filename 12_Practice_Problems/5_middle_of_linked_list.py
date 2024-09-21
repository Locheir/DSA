## Middle of a Singly Linked List

# Write a function to find and return the middle 
# node of a singly linked list. If the list has 
# an even number of nodes, return the second of 
# the two middle nodes.


class Node:
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
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def find_middle(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head
        else:
            if self.length%2 == 0:
                count = 1
                tmp_node = self.head
                while tmp_node:
                    if count == (self.length/2 + 1):
                        return tmp_node
                    tmp_node = tmp_node.next
                    count += 1
            else:
                count = 1
                tmp_node = self.head
                while tmp_node:
                    if count == (self.length//2 + 1):
                        return tmp_node
                    tmp_node = tmp_node.next
                    count += 1
    
    ## Another Way : 
    # The approach, often called the "fast and slow pointer" 
    # technique or "tortoise and hare" algorithm, allows you 
    # to traverse the list only once, instead of first counting 
    # the elements and then accessing the middle one.

    def find_middle2(self):
        slow = self.head
        fast = self.head 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow 