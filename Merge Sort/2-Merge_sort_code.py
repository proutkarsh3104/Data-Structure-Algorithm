
def merge_sort(my_list):
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])   # Takes elements from index 0 up to (but not including) mid_index
    right = merge_sort(my_list[mid_index:])
    return merge(left,right)