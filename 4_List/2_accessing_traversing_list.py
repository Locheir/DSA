## Accessing / Traversing the List : 

# Accessing Elements in List : 
shoppingList = ['Milk','Bread','Cheese','Butter']

print("Second Element in List :",shoppingList[1])
print("First Element in List :",shoppingList[0])
print("Fourth Element in List :",shoppingList[3])


# Check if an object is present in list by using 'in' operator :
if "Milk" in shoppingList:
    print("Milk Exist in the List")


# Traversing the whole List :
for item in shoppingList:
    print(item)


# Anther way of Traversing the whole List : 
for i in range(len(shoppingList)):
    print(shoppingList[i])


# Negative Indexing in Lists :
print("Last Element in List :",shoppingList[-1])
print("Third Last Element in List :",shoppingList[-3])
