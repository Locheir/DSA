### Build-in Operations in Dictionary :

# using 'in' operator :
my_dict = {
    3: 'three',
    1: 'one',
    4: 'four',
    2: 'two',
    11: 'eleven',
    6: 'six',
    9: 'nine'
}

print(3 in my_dict)
print(7 not in my_dict)

# 'in' Operator checks for keys by default.
# if you want to check for values then.
print('three' in my_dict.values())

# 'len()' function in dictionary :
print(len(my_dict))

# all() : returns True only when all the items are true.
# checking if even one key is false or not.
my_dict2 = {
    1: 'firstone',
    False: 'falseone'
}
print(all(my_dict))
print(all(my_dict2))
# if we keep a key as 0 , it will detect 0 as false.

# any() : returns True only when atleast one item is true.
# checking if even one key is true or not.
print(any(my_dict))
print(any(my_dict2))

# sorted() : returns the list of keys in sorted order 
print(sorted(my_dict))