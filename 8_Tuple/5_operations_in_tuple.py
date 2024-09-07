## Tuple Operations and Functions : 

myTuple1 = (1,4,3,2,5)
myTuple2 = (1,2,6,9,8,7)

# '+' Operator : 
print(myTuple1 + myTuple2)

# '*' Operator : 
print(myTuple1*4)

# There are no methods for removing or adding 
# in Tuple as these are immutable in nature.

# count() : counting the number of times a 
# value is present inside the Tuple.
print(myTuple1.count(2))

# index() : finding the index of a specific value.
print(myTuple1.index(5))

# len() : to find the number of elements in tuple.
print(len(myTuple1))

# max() : to find the maximum of all elements in tuple.
print(max(myTuple1))

# min() : to find the minimum of all elements in tuple.
print(min(myTuple1))