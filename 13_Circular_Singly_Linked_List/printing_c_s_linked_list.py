# Printing the Circular Singly Linked List : 

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
            new_node.next = self.head
            self.tail = new_node
        else :
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1

    def __str__(self) :
        tmp_node = self.head 
        if self.head :
            result = ''
            while tmp_node :
                result += str(tmp_node.value)
                tmp_node = tmp_node.next
                if tmp_node == self.head :
                    break
                result += ' -> '
            return result
        else :
            return "Linked List is Empty !"
        
csl = CSLinkedList()
print(csl)
csl.append(11)
csl.append(12)
csl.append(13)
csl.append(14)
print(csl)