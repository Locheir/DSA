# TRAVERSAL IN ARRAY : 
import array 
arr = array.array('i', [1,2,3,4])

def traversalArray(array):
    for i in array:
        print(i)

traversalArray(arr)


# Accessing an element in an array : 
def access_element(arr, index):
    if index > len(arr):
        print("Index out of bounds")
    else : 
        print(arr[index])

arr2 = array.array('i', [1,2,3,4,5,60])
access_element(arr2,5)


# Searching an element in an array : 
def search_element(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

arr3 = array.array('i', [12,33,45,22,17,300])
print(search_element(arr3,22))