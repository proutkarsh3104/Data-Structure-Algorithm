#  Method 1: Using for loop which is very slow with O(n^2) time complexity.
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

#  Method 2: Using Hash Table with dictionary which is very fast with O(n) time complexity.
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False
