from array import *

# 1. Create an array and traverse it.
arr = array('i', [1, 2, 3, 4, 5])

for i in arr:
    print(i)

# 2. Access any individual element in an array through indexes.
arr1 = array('i', [1, 2, 3, 4, 5])
print(arr[0])

# 3. Append any value to the array using append() method.
arr2 = array('i', [22,35,11,7,18])
arr2.append(12)
print(arr2)

# 4. Extend python array using extend() method.
arr3 = array('i', [1,22,43,75,50,89])
arr3.extend([2,3,4])
print(arr3)

# 5. Insert new value in an array using insert() method.
arr4 = array('i', [1,22,43,75,50,89])
arr4.insert(0,99)
print(arr4)

# 6. Add items from list into array using fromlist() method.
x = array('i', [1,2,3,4,5,6,7])
y = [8, 9, 10]
x.fromlist(y)
print(x)

# 7. Remove any array element using remove() method.
arr5 = array('i', [12,34,5,67,81])
arr5.remove(12)
print(arr5)

# 8. Remove the last array using pop() method.
arr6 = array('i', [12,34,15,26,87])
arr6.pop()
print(arr6)

# 9. Fetch any element through it's index using index() method.
arr7 = array('i', [12,34,15,26,87])
print(arr7.index(15))

# 10. Reverse a python array using reverse() method.
arr8 = array('i', [12,32,14,65,67,92,83,63])

def reverse_arr(arr):
    first = 0 
    last = len(arr)-1
    while(first < last):
        temp = arr[first]
        arr[first] = arr[last]
        arr[last] = temp
        first += 1
        last -= 1
    return arr

print(reverse_arr(arr8))

# 11. Get array buffer information through buffer_info() method.
arr9 = array('i', [12,32,14,65,67,92,83,63] )
print(arr9.buffer_info())

# 12. Check for number of occurrences of an element using count() method.
arr10 = array('i', [12,32,14,15,65,67,92,15,83,63])
print(arr10.count(15))

# 13. Convert array to a python list with same element using tolist() method.
arr11 = array('i', [12,32,14,15,65,67,92,15,83,63])
temp_list = arr11.tolist()
print(temp_list)

# 14. Slice Elements from an array.
arr12 =  array('i', [12,32,14,15,65,67,92,15,83,63])
print(arr12[1:4])