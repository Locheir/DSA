### Reverse Key-Value Pairs

# Define a function which takes as a parameter dictionary a
# nd returns a dictionary in which everse the key-value 
# pairs are reversed.

def reverse_dict(my_dict):
    new_dict = {}
    for key, value in my_dict.items():
        new_dict[value] = key
    return new_dict

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(reverse_dict(my_dict))

# Another Solution : 
def reverse_dict2(my_dict):
    return {v: k for k, v in my_dict.items()}