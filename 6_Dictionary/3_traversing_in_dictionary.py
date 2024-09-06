# Traversing in an Array :

myDict = {"name": "Mohit", "age": 21, "address": "pune"}

def traverseDict(dict):
    for key, value in dict.items() : 
        print(f"{key}: {value}")
    
    for key in dict :
        print("Key :",key)

traverseDict(myDict)