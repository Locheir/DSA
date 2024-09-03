# Deleting in a 2D array : 
import numpy as np

arr =  np.array(
    [
     [11, 15, 10, 6],
     [11, 14, 11, 5],
     [12, 17, 12, 8],
     [15, 18, 14, 9]
    ]
)

def deletingIn2DArray(arr, pos, type):
    if type == 'row':
        new_arr = np.array([[0 for j in range(len(arr[0]))] for i in range(len(arr)-1)])
        flag = False
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if i == pos:
                    flag = True
                elif flag == False:
                    new_arr[i][j] = arr[i][j]
                else:
                    new_arr[i-1][j] = arr[i][j]
    elif type == 'column':
        new_arr = np.array([[0 for j in range(len(arr[0])-1)] for i in range(len(arr))])
        for i in range(len(arr)):
            flag = False
            for j in range(len(arr[0])):
                if j == pos:
                    flag = True
                elif flag == False:
                    new_arr[i][j] = arr[i][j]
                else:   
                    new_arr[i][j-1] = arr[i][j]
    return new_arr

print(deletingIn2DArray(arr,1,'column'))