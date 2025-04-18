class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            # Testing is this list is empty
            self.head = new_node  
            self.tail= new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        
        return True

    def pop(self):
        # To chechk if the list is empty
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        
        while(temp.next):
            pre = temp
            temp = temp.next
            
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # To chechk if there is only one node
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return temp
        # return temp.value
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

        
    def pop_first(self):
        # If the node is 
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # 2nd edge case if there is only one element
        if self.length == 0:
            self.tail = None
        return temp
        # return temp.value
    def get(self, index):
        if index<0 or index >= self.length:
            return None
        
        temp = self.head
        # we have _ here as we not printing the variable in the for loop for example we can have i there but we are not using i in the for loop.
        for _ in range(index):
            temp = temp.next
        
        return temp
           # return temp.value
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if index <0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
my_linked_list = LinkedList(0)
my_linked_list.append(2)

my_linked_list.insert(1,1)

my_linked_list.print_list()