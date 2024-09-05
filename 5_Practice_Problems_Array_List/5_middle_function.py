# Write a function called middle that takes a list and returns 
# a new list that contains all but the first and last elements.

lst = [1,93,28,38,20,7]

def middle(lst):
    new_lst = []
    for i in range(1,len(lst)-1):
        new_lst.append(lst[i])
    return new_lst

print(middle(lst))

# Another solution :
def middle_another(lst):
    return lst[1:len(lst)-1]

print(middle_another(lst))