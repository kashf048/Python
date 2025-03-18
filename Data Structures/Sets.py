# A set which is basically a collection with no duplicates.

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)
print(first & second)   # both 
print(first - second)
print(first ^ second)

# print(first[0])     # throw error no index access

if 1 in first:
    print("yes")