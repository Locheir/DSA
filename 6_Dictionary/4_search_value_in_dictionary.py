# Search for a value through a Dictionary :

myDict = {'name': 'Mohit', 'age': 21, 'address': 'Pune'}

def searchDict(dict, target):
    for key in dict:
        if dict[key] == target:
            return key, target
    return 'The value does not exist'

print(searchDict(myDict, 'Pune'))