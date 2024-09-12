class Node : 

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList :

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None : 
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def __str__(self):
        tmp_node = self.head
        if self.head is None :
            return "Linked List is Empty !"
        else :
            result = ''
            while(tmp_node is not None):
                result += str(tmp_node.value)
                if tmp_node.next is not None:
                    result += '->'
                tmp_node = tmp_node.next
            return result
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None : 
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def insert(self, value, pos):
        new_node = Node(value)
        temp_node = self.head
        if pos < 0 or pos > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for i in range(pos-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
l1 = LinkedList()
l1.append(3)
l1.append(4)
l1.append(5)
l1.prepend(2)
l1.insert(33,1)
print(l1)
print(l1.length)