# Accessing an element in 2D Array : 
import numpy as np

arr =  np.array(
    [
     [11, 15, 10, 6],
     [11, 14, 11, 5],
     [12, 17, 12, 8],
     [15, 18, 14, 9]
    ]
)

def accessElements(arr, rowIndex, columnIndex):
    if rowIndex >= len(arr) or columnIndex >= len(arr[0]):
        return "Incorrect Index"
    else:
        return arr[rowIndex][columnIndex]
    
print(accessElements(arr,0,2))
    

# Traversing in a 2D Array : 
arr2 =  np.array(
    [
     [11, 15, 10, 6],
     [11, 14, 11, 5],
     [12, 17, 12, 8],
     [15, 18, 14, 9]
    ]
)

def arrayTraversal(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

arrayTraversal(arr2)

# Searching in an 2D array : 
def searchInArray(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return i,j
    return -1

print(searchInArray(arr2,8))