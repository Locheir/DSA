# Write a function to find the missing number in a given integer array of 1 to 100. 
# The function takes to parameter the array and the number of elements that needs to be in array.  
# For example if we want to find missing number from 1 to 6 the second parameter will be 6.

arr = [1,2,4,3,6,7,8,9,10]
num = 10

def find_missing(arr,num):

    # Find sum of 'n' natural numbers :
    num_sum = num * (num+1) // 2

    # Find sum of all array elements :
    arr_sum = 0
    for i in arr:
        arr_sum += i
    
    # Find the missing Number :
    missing_num = num_sum - arr_sum

    return missing_num

print(f"Missing Number for {arr} is {find_missing(arr,num)}")