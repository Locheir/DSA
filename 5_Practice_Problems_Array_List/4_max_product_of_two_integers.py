# Find the maximum product of two integers in an array where all elements are positive.
arr = [1,7,5,3,6,9]

def max_product(arr):
    max = arr[0]*arr[1]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j] > max:
                max = arr[i]*arr[j]
    return max

print(max_product(arr))

# Another way to get to the answer

def max_product_another(arr):
    max1 = 0
    max2 = 0

    for num in arr:
        # If current number is greater than max1
        # Update max1 and max2
        if num > max1 :
            max2 = max1
            max1 = num
        # If current number is greater than max2 
        # Update max2
        elif num > max2 :
            max2 = num

    return max1*max2

print(max_product_another(arr))