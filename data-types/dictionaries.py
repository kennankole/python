'''
  ######
  #DICTIONARIES#
  ######
   * are indexed by unique keys
   * any immutable data type can used as keys
   * is a key:value pair data type
'''
tel = {'jack': 4098, 'sape': 4139}

# adding element to the dictionary
tel['guido'] = 4127
print(tel)

# Remove an item
del tel['sape']

# Performing list(d) on a dictionary returns a list of all the keys used in the dictionary
dictionary_list = list(tel)
print(dictionary_list)
print(sorted(dictionary_list))


# To check whether a single key is in the dictionary, use the in keyword.
'guido' in tel


# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
new_dictionary = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(new_dictionary)

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
another_dict = dict(sape=4139, guido=4127, jack=4098)

# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
{x: x**2 for x in (2, 4, 6)}

