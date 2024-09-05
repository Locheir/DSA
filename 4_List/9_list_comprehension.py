## Normal List Comprehension : 

prev_list = [1,2,3]
new_list = [i*2 for i in prev_list]
print(new_list)

string1 = "Python"
new_list_str = [i for i in string1]
print(new_list_str)

## Conditional List Comprehension :
# Get all positive numbers 
prev_list2 = [-1, 10 , -20, 2, -90, 60, 45, 20]
new_list2 = [i for i in prev_list2 if i > 0]
print(new_list2)

# Get square of negative numbers 
prev_list3 = [-1, 10 , -20, 2, -90, 60, 45, 20]
new_list3 = [i**2 for i in prev_list3 if i < 0]
print(new_list3)

# Check for consonants 
sentence = 'My name is Mohit Gupta'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

## if-else version of List Comprehension :
# If number is greater than zero then store number
# If number is smaller than zero then store zero
prev_list4 = [-1, 10 , -20, 2, -90, 60, 45, 20]
new_list4 = [number if number > 0 else 0 for number in prev_list4]
print(new_list4)