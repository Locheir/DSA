import numpy as np

arr = np.array(
    [
     [11, 15, 10, 6],
     [11, 14, 11, 5],
     [12, 17, 12, 8],
     [15, 18, 14, 9]
    ]
)

def insert_in_2d_array(arr, nums, pos, type):
    rows = len(arr)
    columns = len(arr[0])
    
    if type == 'column':
        new_arr = np.array([[0 for i in range(columns+1)] for i in range(rows)])

        for i in range(len(new_arr)):
            flag = False

            for j in range(len(new_arr[0])):
                if j == pos :
                    new_arr[i][j] = nums[i]
                    flag = True
                elif flag == False :
                    new_arr[i][j] = arr[i][j]
                else :
                    new_arr[i][j] = arr[i][j-1]

        return new_arr
    
    elif type == 'row':
        new_arr = np.array([[0 for i in range(columns)] for i in range(rows+1)])
        flag = False
        for i in range(len(new_arr)):
            for j in range(len(new_arr[0])):
                if i == pos:
                    new_arr[i][j] = nums[j]
                    flag = True
                elif flag == False:
                    new_arr[i][j] = arr[i][j]
                else:
                    new_arr[i][j] = arr[i-1][j]
        return new_arr
    
    else :
        return "Wrong type specified !"

print(insert_in_2d_array(arr, [12,13,14,15], 1, 'row'))

# OR we can use the in-build function called np.insert()

new_arr = np.insert(arr, 0, [[1,2,3,4]], axis=1)
print(new_arr)