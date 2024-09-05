# Write a function to remove the duplicate numbers 
# on given integer array/list.

def remove_duplicates(arr):
    new_lst = []
    
    for i in arr:
        if i not in new_lst:
            new_lst.append(i)
    
    return new_lst

lst = [1,2,2,3,4,5,5,5,6,4,1]
print(remove_duplicates(lst))

# LeetCode : 26. Remove Duplicates from a sorted array 
def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        withoutDublicates = []
        i = 0
        for value in nums:
            if value not in withoutDublicates:
                nums[i] = value
                withoutDublicates.append(value)
                i = i+1
        
        del nums[i:]
        return i+1