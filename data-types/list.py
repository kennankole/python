'''
Lists basics
'''
my_list = []
# Inserting elements at the end of a list
for i in range(10):
  my_list.append(i)

# List indexs
my_list[0] # gets the first element
my_list[-1] # gets the last element

# Slicing returns a new list
my_list[-3:]

# Lists can be concantenated
my_list + ["hello", "world"]

# The content of lists can be changed
cubes = [1, 8, 17, 65, 125]
cubes[3] = 64
cubes

# Slicing and replacing values
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E'] # from index 2 (included) upto 5 (excluded)
letters

# we can decide to remove these elements entirely from the list
letters[2:5] = []
print(letters)


'''
LIST METHODS
'''
another_list = []

# a. apppend(x)
# Add an item to the end of the list
another_list.append(3)

'''
b. extend(iterable)
add elements from an iterable (e.g., a list, tuple, or string) to the end of a list. 
It modifies the original list in place and does not create a new list
'''
# Example 1: Using extend() with a list
original_list = [1, 2, 3]
additional_elements = [4, 5, 6]

original_list.extend(additional_elements)

print(original_list)

additional_element = "456"
original_list.extend(additional_element) # the individual characters are added to the end of the list
print(original_list)

'''
  c. insert(i, x)
  Inserts an item at a position.
  i is the index, whereas x is the item to be inserted
'''
original_list.insert(2, 500)
print(original_list)

'''
  d. remove(x)
  Removes the first item from the list whose value is equal to x
  It raises an error if x doesn't exist
'''
original_list.remove(500)
print(original_list)

'''
  e. pop([i])
  Removes the item at position i and returns it. 
  If i is not specified, pop() removes and returns the last element.
'''
new_item = original_list.pop(original_list[4])
print(new_item)
new_item = original_list.pop()
print(new_item)

'''
  f. clear()
  Removes all items from the list
'''
original_list.clear()
print(original_list)

'''
  g. index(x)
  Finds the index of the first occurence of an element
'''
print(original_list.index(2))

'''
  h. count(x)
  Returns the number of times x appears in the list
'''
original_list.count(2)

'''
  i. reverse()
  Reverses the elements of the list in place
'''
original_list.reverse()

'''
  j. copy()
  Returns a shallow copy of the list
'''
original_list.copy()

'''
  k. sort(*, key=None, reverse=False)
  Sorts the items of the list in place
'''
original_list.sort()
