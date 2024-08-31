# Case 1 : 
def print_items1(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

print_items1(5,4)
# 
# For this Case, the time complexity is O(a + b)


# Case 2 : 
def print_items2(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)

print_items2(3,4)
# For this Case , the time complexity is O(a*b)