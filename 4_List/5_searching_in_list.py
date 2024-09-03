### Searching for an element in a list : 

myList = [10,20,30,40,50,60,70]

# using in operator : 
target = 31
if target in myList:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

# linear search :
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target: 
            return i
    return -1

print(linear_search(myList, 50))

