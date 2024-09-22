# Inserting at any point in the Linked List : 

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

    def insert(self, index, value) :
        if index > self.length or index < 0 :
            return "Invalid Index given"
        elif index == self.length :
            self.append(value)
        elif index == 0 :
            self.prepend(value)
        else :
            new_node = Node(value)
            tmp_node = self.head
            if tmp_node :
                count = 0
                while tmp_node :
                    if count == index - 1 :
                        break
                    tmp_node = tmp_node.next
                    count += 1

                new_node.next = tmp_node.next
                tmp_node.next = new_node
                self.length += 1

cll = CSLinkedList()
cll.append(20)
cll.append(30)
cll.append(40)
cll.insert(0,10)
print(cll)
cll.insert(2,50)
print(cll)
print(cll.length)
cll.insert(5,100)
print(cll)
print(cll.head.value)
print(cll.tail.value)