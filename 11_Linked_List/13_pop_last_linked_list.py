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
            while(tmp_node):
                result += str(tmp_node.value)
                if tmp_node.next:
                    result += '->'
                tmp_node = tmp_node.next
            return result
        else:
            return "Linked List is Empty"
        
    def pop_last(self):
        tmp_node = self.head
        if self.length == 0:
            return "Cannot pop from an Empty LinkedList"
        elif self.length == 1:
            result = self.head.value
            self.head = None
            self.tail = None
        else:
            tmp_node = self.head
            while(tmp_node.next != self.tail):
                tmp_node = tmp_node.next
            result = self.tail.value
            self.tail = tmp_node
            self.tail.next = None
        self.length -= 1
        return result

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
print(l1)
print(l1.pop_last())
print(l1)
print(l1.pop_last())
print(l1)
print(l1.pop_last())
print(l1)
print(l1.pop_last())
print(l1)