# A tuple is basically a read only list. We can use it to contain a sequence of object but we cannot modify this sequence

# point = 1     Integer
# point = 1,    tuple
# point = ()    tuple  
# point = 1, 2  tuple  
# point = (1, 2) + (3, 4)   # concatate
# point = (1, 2) * 3      # repeatition
# point = tuple([1, 2])   # list to tuple
# point = tuple("Hello World")
point = (1, 2, 3)
print(type(point))
print(point)
print(point[0])
print(point[0:2])
print(point[-1])
x, y, z = point
if 10 in point:
    print("exists")

# point[0] = 10   tuples are immutable, meaning their contents cannot be changed after they are created. 
