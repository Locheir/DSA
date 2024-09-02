# Deleting from an array : 
import array 

def delete_element(arr, ele):

    new_arr = array.array(arr.typecode, [0 for i in range(len(arr)-1)])
    # replace = ele
    flag = False 

    for i in range(len(new_arr)):
        if arr[i] == ele:
            flag = True

        if flag == True : 
            new_arr[i] = arr[i+1]
        else :
            new_arr[i] = arr[i]

    if flag == False:
        return "Element not Found!"
    else :
        return new_arr

arr = array.array('i', [1, 2, 3, 4, 5, 6])
print(delete_element(arr, 3))