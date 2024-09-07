## Searching for an element in a Tuple : 

newTuple = ('a', 'b', 'c', 'd', 'e')

# Searching using 'in' operator : 
print('a' in newTuple)
print('f' in newTuple)

# Searching using 'index()' function : 
print(newTuple.index('c'))
# If element not found the 
# method will raise error.
# print(newTuple.index('g'))

# Example making a custom function : 
def searchTuple(p_tuple, element):
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == element:
            return f"The {element} found at index {i}"
    return f"The {element} was not found"
print(searchTuple(newTuple, 'a'))
print(searchTuple(newTuple,'g'))