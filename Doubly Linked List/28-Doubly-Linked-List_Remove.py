def remove(self, index):
    if index < 0 or index >= self.length:
        return None
    if index == 0:
        return self.pop_first()
    if index == self.length - 1:
        return self.pop()
    temp = self.get(index)
    
    temp.next.prev = temp.prev
    temp.prev.next = temp.next
    temp.next = None
    temp.prev = None
    
    self.length -= 1
    return temp