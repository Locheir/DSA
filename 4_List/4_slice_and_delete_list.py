### Slicing and Deleting from the list : 
myList = [1,2,3,4,5,6,7,8,9]

# Slicing from the list.
print(myList[0:4])

## Deleting from a list.
# pop() function by default deletes the last element.
# or you can give the function the index of the specific number.
myList = [1,2,3,4,5,6,7,8,9]
myList.pop(1)
print(myList)

# del method
myList = [1,2,3,4,5,6,7,8,9]
del myList[0]
print(myList)

# remove() function is used to delete by giving a number.
myList = [10,23,3,14,52,68,75,8,9]
myList.remove(52)
print(myList)
