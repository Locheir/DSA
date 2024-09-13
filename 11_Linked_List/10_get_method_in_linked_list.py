# Get Method : 
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
        
    def get(self, index):
        if index > self.length or index < 0:
            return -1
        else :
            tmp_node = self.head
            if self.head:
                count = 0
                while(tmp_node):
                    if count == index:
                        return tmp_node.value
                    count +=1
                    tmp_node = tmp_node.next
            else:
                return "Linked List is Empty"
            
l1 = LinkedList()

l1.append(1)
l1.append(88)
l1.append(7)
l1.append(5)
l1.append(2)
l1.append(4)

print(l1.get(1))