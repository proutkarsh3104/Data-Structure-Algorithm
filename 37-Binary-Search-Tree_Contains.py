def contains(self, value):
    # We dont need this line in our contains method.
    # if self.root is None:
    #     return False
    temp = self.root
    while temp is not None:
        if value < temp.value:
            temp = temp.left
        elif value > temp.value:
            temp = temp.right
        # If we find the value then we do this.
        else:  
            return True
    return False