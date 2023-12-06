'''
Using Lists as Stacks (FIFO)

To add an item to the stack use append()
To retreive an item from the top of the stack use pop()
'''

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
popped = stack.pop()
print(popped)

'''
Using Lists as Queues (FIFO)

While appends and pops from the end of list are fast, 
doing inserts or pops from the beginning of a list is slow 
(because all of the other elements have to be shifted by one).

we therefore use deque that is designed to have fast appends and pops from both ends
'''

from collections import deque

queue = deque(['Eric', 'John', 'Michael'])

# Adding elements to the queue
queue.append('Terry')
queue.append('Graham')

# Removing elements from the queue
removed = queue.popleft()
print(removed)

'''
List Comprehensions
  * provide a concise way to create lists.
  * makes new lists where each element is the result of some operations 
  * applied to each member of another sequence or iterable, 
  * or to create a subsequence of those elements that satisfy a certain condition.
'''

squares1 = []
for x in range(10):
  squares1.append(x ** 2)


squares2 = list(map(lambda x: x ** 2, range(10)))

squares3 = [x ** 2 for x in range(10)]

combined = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

vec = [-4, -2, 0, 2, 4]

# Create a new list with the values doubled
doubled = [x * 2 for x in vec]

# filter the list to excluded negative number
positive = [x for x in vec if x >= 0]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
capitalized = [fruits.strip().capitalize() for fruits in freshfruit]

# Flatten a list
vecs = [[1,2,3], [4,5,6], [7,8,9]]
flattened = [num for elem in vecs for num in elem]

from math import pi 
pi_values = [str(round(pi, i)) for i in range(1, 6)]


# Nest List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# We can then transpose the matrix using list comprehension
transposed_1 = [[row[i] for row in matrix] for i in range(4)]

# or
transposed_list = []
for i in range(4):
  print(i)
  transposed_list.append([row[i] for row in matrix])
  
# alternatively, we should use built-in functions 
transposed_3 = list(zip(*matrix))
print(transposed_3)