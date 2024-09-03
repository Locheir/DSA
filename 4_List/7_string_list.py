### String and List : 

## String to List :
# using list() :
str1 = 'spam'
l1 = list(str1)
print(l1)

# using split() :
a = 'spam spam spam'
l2 = a.split()
print(l2)

b = 'spam-spam1-spam3'
delimiter = '-'
l3 = b.split(delimiter)
print(l3)

## List to String :
# using join()
l4 = ['spam', 'spam2', 'spam3', 'spam4']
delimiter = '-'
c = delimiter.join(l4)
print(c)