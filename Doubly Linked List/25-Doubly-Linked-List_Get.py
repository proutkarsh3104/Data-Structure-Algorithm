def get(self, index):
    if index < 0 or index >= self.length:
        return None
    temp = self.head
    if index < self.length/2:
        for _ in range(index):
            temp = temp.next
    else:
        temp = self.tail
        for _ in range(self.length - 1, index, -1):
            temp = temp.prev
    return temp
    