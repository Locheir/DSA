# Common Keys
# Define a function with takes two dictionaries as 
# parameters and merge them and sum the values of common

def merge_dicts(dict1, dict2):
    # TODO
    merge_dict = {}
    merge_dict = dict2.copy()
    for key in dict1:
        if key not in merge_dict:
            merge_dict[key] = dict1[key]
        else:
            merge_dict[key] += dict1[key]
    return merge_dict

dict1 = {'a': 1, 'b': 2, 'c': 3,'e':1}
dict2 = {'b': 3, 'c': 4, 'd': 5, 'a':2}
print(merge_dicts(dict1, dict2))
