### Python Tuple : 

# A Tuple is an immutable sequence of Python objects.
# Tuples are also comparable and hashable.

t1 = 'a','b','c','d'
print(t1)

# Generally we give the elements inside paranthesis : 
t2 = (1, 2, 3, 4)
print(t2)

# If we have only one element in a tuple.
# Then it will be taken as string so we have 
# to give a comma after the single element.
# See the difference between t3 and t4.
t3 = ('a')
print(t3)
t4 = ('a',)
print(t4)