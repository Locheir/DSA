## Concatenate

# Write a function that takes a tuple 
# of strings and concatenates them, 
# separating each string with a space.

def concatenate_strings(input_tuple):
    string = ''
    n = len(input_tuple)
    for i in range(n):
        if n-1 == i:
            string += str(input_tuple[i])
        else:
            string += input_tuple[i]+' '
    return string

input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)  

# Another Solution : 
def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)
