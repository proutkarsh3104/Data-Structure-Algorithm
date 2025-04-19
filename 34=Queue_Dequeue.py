def dequeue(self):
    if self.length == 0:
        return None
    temp = self.first
    if self.length == 1:
        self.first = None
        self.last = None
    else:
        self.first = self.first.next
        temp.next = None
    self.length -= 1
    return temp