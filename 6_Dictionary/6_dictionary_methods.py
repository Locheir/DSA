### Dictionary Methods :

# copy() : used to create a shallow copy of dictionary.
# Changes in shallow copy will not effect original copy.
myDict = {'name': 'Mohit', 'age': 21, 'address': 'Pune'}
print(myDict)
newDict = myDict.copy()
print(newDict)


# fromkeys() : creates a new dictionary with 
# given sequence and value provided by user.
# Syntax : fromkeys([]sequence, value)
myDict2 = {}.fromkeys([1, 2, 3], 0)
print(myDict2)


# get() : returns the value for specified key if it exists.
# if value is not found returns None.
# syntax : get(key, value)
myDict3 = {'name': 'Mohit', 'age': 21, 'address': 'Pune'}
found_or_not = myDict3.get('name', None)
print(found_or_not) 


# items() : returns a list of tuple containing key 
# and value pair for each element in dictionary.
myDict4 = {'name': 'Mohit', 'age': 21, 'address': 'Pune'}
print(myDict4.items())


# keys() : returns a list of all the keys present in dictionary.
myDict5 = {'name': 'Mohit', 'age': 21, 'address': 'Pune'}
print(myDict5.keys())


# setdefault() : returns value for specified key if it 
# exists otherwise the specified key is created in 
# dictionary with the value as default value given.
myDict6 = {'name': 'Mohit', 'age': 22}
print(myDict6.setdefault('rollno',17))
print(myDict6)


# values() : returns a list of all the values present in dictionary.
myDict7 = {'name': 'Mohit', 'age': 22, 'rollno': 17}
print(myDict7.values())


# update() : if key is in the dictionary value get's updated 
# if the key is not present a new key-value pair is created.
myDict7 = {'name': 'Mohit', 'age': 22, 'rollno': 17}
newDict = {'a': 1, 'b': 2, 'c': 3}
myDict7.update(newDict)
print(myDict7)