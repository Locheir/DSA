# O(n^2) Time Complexity : 

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(5)

# In the case where there is a loop inside the loop
# Time Complexity => n*n => n^2

# This time complexity is considered bad.



# O(n^3) Time Complexity : 

def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

print_items(5)

# Time Complexity => n*n*n => n^3
# For this case as well we write it as n^2 time complexity.