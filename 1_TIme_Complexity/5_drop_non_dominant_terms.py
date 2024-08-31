# Dropping the non-dominant terms : 

# For example if we have the code given below 

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)

# If we try to calculate the time complexity for the above function 
# For the loop inside loop part time complexity is O(n^2)
# For the single loop part the time complexity is O(n)

# The Total Time Complexity is O(n^2 + n)

# if we put a large number as n 
# Let say we put n = 10000
# Then n^2 = 10000^2 = 100000000
# and n = 10000
# Here compared to n^2 , n is very small hence we drop it.
# This concept is known as dropping non-dominant terms.