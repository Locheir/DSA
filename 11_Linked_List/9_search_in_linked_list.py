# Search in Linked List 

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
        if self.head:
            result = ''
            while(tmp_node is not None):
                result += str(tmp_node.value)
                if tmp_node.next:
                    result += '->'
                tmp_node = tmp_node.next
            return result
        else:
            return "Linked List is Empty"
        
    def search(self, value):
        tmp_node = self.head
        if self.head:
            count = 0
            while(tmp_node):
                count +=1
                if tmp_node.value == value:
                    return count-1
                tmp_node = tmp_node.next
        else:
            return -1

l1 = LinkedList()
l1.append(1)
l1.append(88)
l1.append(7)
l1.append(5)
l1.append(2)
l1.append(4)
print(l1)
print(l1.search(2))