# Prepend in Circular Linked List : 

class Node : 

    def __init__(self, value) :
        self.value = value
        self.next = None

class CSLinkedList : 

    def __init__(self) :
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value) :
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
        if tmp_node :
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
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head :
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        else :
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        self.length += 1

csl = CSLinkedList()
print(csl)
csl.append(11)
csl.append(12)
csl.append(13)
print(csl)
csl.prepend(10)
print(csl)
print(csl.length)