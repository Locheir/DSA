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
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        tmp_node = self.head
        if tmp_node:
            result = ''
            while tmp_node:
                result += str(tmp_node.value)
                if tmp_node.next:
                    result += '->'
                tmp_node = tmp_node.next
            return result
        else:
            return "Linked List is Empty !"
        
    def pop_first(self):
        if self.length == 0:
            return "Cannot Delete as Linked List is Empty"
        elif self.length == 1:
            result = self.head.value
            self.head = None
            self.tail = None
        else:
            tmp_node = self.head
            self.head = self.head.next
            result = tmp_node.value
            tmp_node.next = None
        self.length -= 1
        return result

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
print(l1)
l1.delete_all()
print(l1)