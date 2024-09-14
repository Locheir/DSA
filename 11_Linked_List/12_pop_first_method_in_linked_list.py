class Node :

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList :
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def append(self, value):
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.lenght += 1

    def __str__(self):
        tmp_node = self.head
        if tmp_node:
            result = ''
            while(tmp_node):
                result += str(tmp_node.value)
                if tmp_node.next:
                    result += '->'
                tmp_node = tmp_node.next
            return result
        else:
            return "Linked List is Empty"
        
    def pop_first(self):
        if self.lenght == 0:
            return "Cannot Delete from Empty Linked List"
        elif self.lenght == 1:
            result = self.head.value
            self.head = None
            self.tail = None
        else:
            tmp_node = self.head
            self.head = tmp_node.next
            result = tmp_node.value
            tmp_node.next = None
        self.lenght -= 1
        return result
l1 = LinkedList()
l1.append(1)
print(l1)
print(l1.pop_first())
print(l1)