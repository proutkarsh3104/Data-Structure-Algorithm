def pop_first(self):
    if self.length == 0:
        return None
    temp = self.head
    if self.length == 1:
        self.head = None
        self.tail = None
    else:
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        
    self.length -= 1
    return temp
