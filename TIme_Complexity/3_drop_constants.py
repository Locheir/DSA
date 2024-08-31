# Lets say in we are having two different for loop in the same function : 

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(5)

# If we find the time complexity of this it will be :
# First Loop -> n time complexity
# Second Loop -> n time complexity 
# Total Time Complexity = n + n = 2n

# But for this type of situation we drop the constant with n.
# So the actual time complexity is not O(2n) but O(n).