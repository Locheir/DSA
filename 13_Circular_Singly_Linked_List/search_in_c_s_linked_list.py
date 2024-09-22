## Search :

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
        if self.head :
            result = ''
            while (tmp_node) :
                result += str(tmp_node.value)
                tmp_node = tmp_node.next
                if tmp_node == self.head :
                    break
                result += ' -> '
            return result
        else :
            return "Linked List is Empty !"
        
    def search(self, value) :
        tmp_node = self.head
        if self.head : 
            count = 0
            while tmp_node :
                if tmp_node.value == value :
                    return count
                tmp_node = tmp_node.next 
                count +=1
                if tmp_node == self.head :
                    return -1
        else:
            return -1
        
csl = CSLinkedList()
csl.append(1)
csl.append(10)
csl.append(11)
csl.append(21)
csl.append(65)
print(csl)
print(csl.search(21))
print(csl)
