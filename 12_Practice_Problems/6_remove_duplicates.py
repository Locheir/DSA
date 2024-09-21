## Remove Duplicates from a Singly Linked List

# Given a singly linked list, write a function that 
# removes all the duplicates. use this linked list .

# Original Linked List - "1 -> 2 -> 4 -> 3 -> 4 -> 2"

# Result Linked List - "1 -> 2 -> 4 -> 3"

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

    def __str__(self) :
        if self.head:
            result = ''
            tmp_node = self.head
            while tmp_node :
                result += str(tmp_node.value)
                if tmp_node.next:
                    result += '->'
                tmp_node = tmp_node.next
            return result
        else:
            return 'Linked List is Empty'
        
    def remove_duplicates(self):
        if self.head is None:
            return 
        
        unique_values = set()
        tmp_node = self.head
        unique_values.add(tmp_node.value)

        while tmp_node.next:
            if tmp_node.next.value in unique_values:
                tmp_node.next = tmp_node.next.next
                self.length -= 1
            else:
                unique_values.add(tmp_node.next.value)
                tmp_node = tmp_node.next
  
l1 = LinkedList()
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(2)
l1.append(6)
l1.append(6)
l1.append(7)
l1.append(3)
print(l1)
l1.remove_duplicates()
print(l1)