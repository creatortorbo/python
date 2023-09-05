# creating an empty set 
b = set ()
print(type(b))

# adding values to an empty set 
b.add(4)
b.add(5)
b.add(4)
b.add(6) # adding the value repeating does not change a set
b.add(8)
b.add((4,5,6))

print(b)