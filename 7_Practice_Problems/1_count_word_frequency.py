# Count Word Frequency
# Define a function to count the frequency 
# of words in a given list of words.

def count_word_frequency(words):
    # TODO
    count_dict = {}
    for word in words:
        if word not in count_dict.keys():
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    return count_dict

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words))