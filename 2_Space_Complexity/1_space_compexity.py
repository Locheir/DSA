# So just like Time Complexity we also have Space Complexity
# It is also very important to learn about space complexity

def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)

print(sum(5))

# The above funtion is a recursive function
# When we execute the above code a call stack is generated 
# which consumes a lot of memory 