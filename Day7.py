# SETS AND DICTIONARIES

# SETS - an unordered collection of unique elements
s={1,2,3,4,5}
print(s)
print(type(s))

# METHODS
# 1.add()-adds an element to the set
s.add(6)
print(s)

# 2.remove()-removes the specified element from the set
s.remove(6)
print(s)

# 3.pop()-removes and returns an arbitrary element from the set
s.pop()
print(s)

# 4.clear()-removes all elements from the set
s.clear()
print(s)

# 5.copy()-returns a shallow copy of the set
s={1,2,3,4,5}
s_copy=s.copy()
print(s_copy)

# 6.delete()-deletes the set
del s

# 7.update()-updates the set with elements from another set
s1={1,2,3}
s2={3,4,5}
s1.update(s2)
print(s1)

# 8.discard()-removes the specified element from the set if it is present
s1.discard(3) 
print(s1)

# SETS OPERATIONS

# 1.union()-returns a new set with elements from both sets
s1={1,2,3}
s2={3,4,5}
print(s1.union(s2))

# 2.intersection()-returns a new set with elements common to both sets
print(s1.intersection(s2))

# 3.difference()-returns a new set with elements in the first set but not in the second
print(s1.difference(s2))

# 4.symmetric_difference()-returns a new set with elements in either set but not in both
print(s1.symmetric_difference(s2))  

# 5.issubset()-returns True if all elements of the first set are in the second set
print(s1.issubset(s2))

# 6.issuperset()-returns True if all elements of the second set are in the first set
print(s1.issuperset(s2))    

# DICTIONARIES - a collection of key-value pairs
d={'a':1,'b':2,'c':3}
print(d)
print(type(d))

# METHODS
# 1.keys()-returns a list of all keys in the dictionary
print(d.keys())

# 2.values()-returns a list of all values in the dictionary
print(d.values())

# 3.items()-returns a list of all key-value pairs in the dictionary
print(d.items())

# 4.get()-returns the value for the specified key
print(d.get('a'))

# 5.update()-updates the dictionary with key-value pairs from another dictionary
d.update({'d':4})
print(d)

# 6.pop()-removes the specified key and returns its value
d.pop('d')
print(d)

# 7.clear()-removes all key-value pairs from the dictionary
d.clear()
print(d)

# 8.popitem()-removes and returns an arbitrary key-value pair from the dictionary
d={'a':1,'b':2,'c':3}       
print(d.popitem())

# 9.copy()-returns a shallow copy of the dictionary
d_copy=d.copy() 
print(d_copy)

# 10.setdefault()-returns the value of the specified key. If the key does not exist, insert the key with the specified value
print(d.setdefault('a', 10))    