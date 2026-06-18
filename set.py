s = {1,2,3}
print(s)

#Adding Element
s.add(4)
print(s)

#Removing element
s.pop()
print(s)

s.remove(3) #Removes the element but throws an error if it doesn't find it
#s.remove(44)
s.discard(44) #Doesn't throw an error
print(s)

#Set Methods and Frozen Set
s = frozenset({1,2,3,4,5})
print(len(s))
print(type(s))

#Methods
a = {1,2,3,4}
b = {2,3,5,6}

print(a.symmetric_difference(b))
