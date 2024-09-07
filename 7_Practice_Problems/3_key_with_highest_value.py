### Key with the Highest Value

# Define a function which takes a dictionary as a 
# parameter and returns the key with the highest 
# value in a dictionary.

def max_value_key(my_dict):
    max = float('-inf')
    max_key = None
    for key in my_dict:
        if my_dict[key] > max:
            max = my_dict[key]
            max_key = key 
    return max_key

my_dict = {'a': 5, 'b': 9, 'c': 2, 'd': 7, 'e': 11}
print(max_value_key(my_dict))

# Another way of doing the problem : 
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)