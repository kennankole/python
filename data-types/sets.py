'''
  ######
  #SETS#
  ######
   * A set is an unordered collection with no duplicate elements.
   *  support mathematical operations like;
      a. union
      b. intersection
      c. difference 
      d. symmetric difference
'''

# Creating a set
# {} or the set() function can be used to create sets. 
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# However, you cannot create an empty set using {}
a = set('abracadabra')
b = set('alacazam')

# Set operations

# 1. get letters in a but not in b
print(a - b)

# 2. letters in a or b or both
print(a | b)

# 3. letters in a or b but not both
print(a ^ b)

# 4. letters in both a and b
print(a & b)

# Also supports set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)