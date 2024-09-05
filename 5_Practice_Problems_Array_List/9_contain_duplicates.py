# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):

    for i, value in enumerate(nums):
        temp = value
        del nums[i]
        if temp in nums:
            return True
    return False