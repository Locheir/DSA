# INSERTION IN ARRAY : 
import array 

my_array = array.array('i',[1,2,3,4])
print(my_array)

my_array.insert(5,6)
print(my_array)


## Making a function to insert in an array.
# def insert_at_(arr,pos,num):
#     replace = num
#     flag = False
#     for i in range(len(arr)):
#         if i == pos :
#             flag = True
        
#         if flag == True :
#             temp = arr[i]
#             arr[i] = replace
#             replace = temp

#         if i == len(arr)-1:
#             arr[i+1] = replace
#     print(arr)
#
# arr = array.array('i', [1,2,3,4,5,6])
# insert_at_(arr,2,7)
#
# There are some problems in the above code

## Making a Function to insert an element in any position in array :
def insert_at_(arr,pos,num):

    new_arr = array.array(arr.typecode , [0 for _ in range(len(arr)+1)])

    replace = num
    flag = False 

    for i in range(len(arr)):

        if i == pos: 
            flag = True
        
        if flag == True:
            temp = arr[i]
            new_arr[i] = replace
            replace = temp
        else : 
            new_arr[i] = arr[i]

    new_arr[len(arr)] = replace

    return new_arr

arr = array.array('i', [1,2,3,4,5,6])
print(insert_at_(arr,2,7))
