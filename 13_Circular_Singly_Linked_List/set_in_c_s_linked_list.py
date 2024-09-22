## Set : 

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
            new_node.next = new_node
        self.length += 1

    def prepend(self, value) :
        new_node = Node(value) 
        if self.head :
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        else : 
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
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
        
    def set(self, index, value) :
        if index < 0 or index >= self.length :
            return "Invalid Index Value"
        else : 
            new_node = Node(value)
            
            tmp_node = self.head 
            for _ in range(index):
                tmp_node = tmp_node.next 
            tmp_node.value = value

csl = CSLinkedList()
csl.append(11)
csl.append(12)
csl.append(13)
csl.append(14)
csl.append(15)
print(csl)
csl.set(2,88)
print(csl)
csl.set(4,99)
print(csl)