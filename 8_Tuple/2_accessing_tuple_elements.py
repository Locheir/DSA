## Access Elements in a Tuple : 

newTuple = ('a', 'b', 'c', 'd', 'e')
print(newTuple[0])
print(newTuple[-1])
print(newTuple[3])

## Access Elements using slice operator : 
# Slice(start : stop : step_size)
print(newTuple[:-2])
print(newTuple[::2])

# As Tuple is not mutable we cannot change
# any value inside it as it will give error.
# newTuple[0] = 'f'