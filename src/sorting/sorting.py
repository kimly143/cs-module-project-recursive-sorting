# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    aindex = 0
    bindex = 0
    for i in range(0, elements):
        if aindex >= len(arrA):
            merged_arr[i] = arrB[bindex]
            bindex += 1
        elif bindex >= len(arrB):
            merged_arr[i] = arrA[aindex]
            aindex += 1
        elif arrA[aindex] < arrB[bindex]:
            merged_arr[i] = arrA[aindex]
            aindex += 1
        else:
            merged_arr[i] = arrB[bindex]
            bindex += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = []
    right = []
    for i in range(0, len(arr)):
        if i < middle:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

