# Pairs :
# Write a function to find all pairs of an integer array whose 
# sum is equal to a given number. Do not consider commutative pairs.

def pair_sum(myList, sum):
    # TODO
    result = []
    for i in range(len(myList)):
        for j in range(i,len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(f"{myList[i]}+{myList[j]}")
    return result

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.nums2[index] += val

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        count = 0
        for val1 in self.nums1 :
            for val2 in self.nums2 :
                if val1 + val2 == tot:
                    count += 1
        return count
    
    def show(self):
        print(self.nums1)
        print(self.nums2)

obj = FindSumPairs([1,1,2,2,2,3], [1,4,5,2,5,4])
obj.add(3,2)
param_2 = obj.count(4)
print(param_2)