## Pop Method : 

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

    def __str__(self) :
        if self.head :
            tmp_node = self.head 
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
    
    def pop_first(self) :
        if self.length == 0 :
            popped_node = self.head 
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node
        if self.head :
            popped_node = self.head
            tmp_node = self.head.next 
            self.tail.next = tmp_node
            self.head.next = None
            self.head = tmp_node
            self.length -= 1
            return popped_node
        else : 
            return None
        
csl = CSLinkedList()
csl.append(11)
csl.append(12)
csl.append(13)
csl.append(14)
csl.append(15)
print(csl)
print(csl.pop_first())
print(csl)