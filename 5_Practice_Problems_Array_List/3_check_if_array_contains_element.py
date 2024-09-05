# Check if an array contains an element or not.
import numpy as np

arr =np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def findNumber(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

print(findNumber(arr,10))