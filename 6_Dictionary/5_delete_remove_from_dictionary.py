### Removing or Deleting an element from a Dictionary :

myDict = {'name': 'Mohit', 'age': 21, 'address': 'Pune', 'education': 'pursuing masters'}
print(myDict)

# Deleting a value with a specific key : 
del myDict['age']
print(myDict)

# Deleting using pop() method :
# If the key is not found we give the second parameter as None.
removed_element = myDict.pop('education', None)
print(myDict)
print(removed_element)

# Deleting using popitem() method :
# popitem() deletes the last element that was inserted in Dictionary.
removed_last_item = myDict.popitem()
print(myDict)
print(removed_last_item)

# Deleting using clear() method :
# clear() method deletes all elements in dictionary.
new_dict = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
new_dict.clear()
print(new_dict)