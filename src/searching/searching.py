# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1
    
    middle = (start + end) // 2
    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binary_search(arr, target, middle + 1, end)
    else:
        return binary_search(arr, target, start, middle - 1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    reverse = arr[0] > arr[-1]
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            if reverse:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if reverse:
                start = middle + 1
            else:
                end = middle - 1
    
    return -1
