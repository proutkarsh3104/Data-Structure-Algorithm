def set_item(self, key, value):
    index = self._hash(key)
    if self.data_map[index] == None:
        self.data_map[index] = []
    self.data_map[index].append((key, value))
        
    