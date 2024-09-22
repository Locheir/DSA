# Pop Last Method  :
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
        
    def pop_last(self) :
        if self.head :
            if self.length == 1 :
                popped_node = self.head
                self.head = None
                self.tail = None
                self.length = 0
                return popped_node
            else :
                tmp_node = self.head
                while tmp_node :
                    if tmp_node.next == self.tail :
                        break
                    tmp_node = tmp_node.next
                popped_node = self.tail
                tmp_node.next = self.head
                self.tail.next = None
                self.tail = tmp_node
                return popped_node
        else :
            return None
        
csl = CSLinkedList()
csl.append(10)
csl.append(11)
csl.append(12)
csl.append(13)
csl.append(14)
print(csl)
print(csl.pop_last())
print(csl)
