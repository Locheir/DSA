## Printing all the elements in Linked List : 

class Node : 
    
    def __init__(self, value):                 # O(1)
        self.value = value
        self.next = None

class LinkedList :

    def __init__(self):                        # O(1)
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):                   # O(1)
        new_node = Node(value)
        if self.head is None : 
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node 
        self.length += 1

    def show(self):                            # O(n)
        if self.head is None : 
            print("Linked List is Empty !")
        else:
            temp_node = self.head
            while(temp_node is not None):
                print(temp_node.value,"-> ", end='')
                temp_node = temp_node.next
            print()

    def __str__(self):                         # O(n)
        if self.head is None : 
            return "Linked List is Empty !"
        else:
            temp_node = self.head
            result = ''
            while(temp_node is not None):
                result += str(temp_node.value)
                if temp_node.next is not None : 
                    result += ' -> '
                temp_node = temp_node.next
            return result
        
    def insert_at_beginning(self, value):      # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head
            self.head = new_node
        self.length += 1

new_ll = LinkedList()

new_ll.append(10)
new_ll.append(11)
new_ll.append(12)
new_ll.show()

new_ll.append(13)
new_ll.show()

new_ll2 = LinkedList()
new_ll2.show()
print(new_ll2)

new_ll2.append(1)
new_ll2.append(2)
new_ll2.append(3)
new_ll2.append(4)
new_ll2.append(5)

print(new_ll2)
print(new_ll2.length)
new_ll2.insert_at_beginning(0)
print(new_ll2)
print(new_ll2.length)