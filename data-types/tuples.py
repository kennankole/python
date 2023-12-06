'''
 **Tuple**
    a sequence data type
    consists of a number of values seperated by commas
    they are immutable like string
    
  >> It is not possible to assign to the individual items of a tuple, 
    however it is possible to create tuples which contain mutable objects, 
    such as lists.
'''
t = 1235, 7439, "hello"

# They can be nested
u = t, (1, 2, 3, 5, 6)

# upacking
x, y, z = t
