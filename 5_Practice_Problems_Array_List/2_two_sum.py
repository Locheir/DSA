# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

arr = [1,2,3,8,4]
target = 10
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == 10:
                return i,j
    return -1

# Another way to solve the problem
def two_sum_another(arr, target):
    seen = {}
    for i,element in enumerate(arr) : 
        temp = target - element
    
        if temp in seen :
            return [seen[temp], i]
        
        seen[element] = i

    return []

print(two_sum_another(arr,target))  

        
