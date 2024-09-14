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
            while (tmp_node):
                result += str(tmp_node.value)
                if tmp_node.next:
                    result += '->'
                tmp_node = tmp_node.next
            return result
        else:
            return "Linked List is Empty !"

    def pop_last(self):
        tmp_node = self.head
        if self.lenght == 0:
            return "Cannot pop from an Empty LinkedList"
        elif self.lenght == 1:
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
        self.lenght -= 1
        return result    
    
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

    def get(self, index):
        if index > self.lenght or index < 0:
            return -1
        else :
            tmp_node = self.head
            if self.head:
                count = 0
                while(tmp_node):
                    if count == index:
                        return tmp_node
                    count +=1
                    tmp_node = tmp_node.next
            else:
                return "Linked List is Empty"

    def remove(self, index):
        if index >= self.lenght or index < 0:
            return None
        if index == self.lenght-1:
            return self.pop_last()
        if index == 0:
            return self.pop_first()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.lenght -= 1
        return popped_node


l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
print(l1)
l1.remove(2)
print(l1)