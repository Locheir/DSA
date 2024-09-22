## Get Method : 

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
    
    def get(self, index) :
        tmp_node = self.head 
        if index < 0 or index >= self.length :
            return -1
        if tmp_node :
            count = 0
            while tmp_node :
                if count == index :
                    return tmp_node.value
                tmp_node = tmp_node.next
                if tmp_node == self.head : 
                    break
                count += 1
            return -1
        else :
            return -1
        
csl = CSLinkedList()
csl.append(11)
csl.append(12)
csl.append(13)
csl.append(14)
csl.append(15)
print(csl)
print(csl.get(3))
print(csl.get(5))