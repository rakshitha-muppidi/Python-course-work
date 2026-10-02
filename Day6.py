# Lists and tuple

# Lists
l=[1,2,3,4,5]
print(l)
print(type(l))

# Methods
# 1.append()-adds a single element to the end of the list
a=[10]
a.append(20)
a.append([30,40])
print(a)

# 2.extend()-adds all elements from another list to the end of the list
a.extend([50,60,70])
print(a)

# 3.insert(index,element)-inserts the specified element at the specified index
a.insert(2,100)
print(a)

# 4.remove(element)-removes the specified element from the list
a.remove(100)
print(a)

# 5.pop()-removes the last element from the list
a.pop()
print(a)

# 6.clear()-removes all elements from the list
a.clear()
print(a)

# 7.index(element)-returns the index of the specified element
a=[10,20,30,40,50]
print(a.index(30))

# 8.count(element)-returns the number of occurrences of the specified element
a=[10,20,30,40,50,10,20,30] 
print(a.count(10))

# 9.sort()-sorts the list in ascending order
a=[30,10,20,50,40]
a.sort()
print(a)

# 10.reverse()-reverses the order of the list
a.reverse()
print(a)

# 11.copy()-returns a shallow copy of the list
a=[10,20,30,40,50]
b=a.copy()
print(b)
# list functions
# 1.len()-returns the number of elements in the list
a=[10,20,30,40,50]  
print(len(a))

# 2.sum()-returns the sum of all elements in the list
a=[10,20,30,40,50]
print(sum(a))

# 3.max()-returns the maximum element in the list
a=[10,20,30,40,50]
print(max(a))

# 4.min()-returns the minimum element in the list
a=[10,20,30,40,50]
print(min(a))

# 5.sorted()-returns a new sorted list from the elements of the list
a=[30,10,20,50,40]
print(sorted(a))

# TUPLE -an ordered collection of elements which is immutable
t=(1,2,3,4,5)
print(t)
print(type(t))

# METHODS
# 1.count()-returns the number of occurrences of the specified element
t=(1,2,3,4,5,1,2,3) 
print(t.count(1))

# 2.index()-returns the index of the specified element
print(t.index(3))
