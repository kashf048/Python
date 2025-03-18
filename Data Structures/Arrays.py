# Use array only if you're dealing with a large sequence of numbers and you encounter performance problems.

from array import array

numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.append(5)
numbers.insert(5, 6)
numbers.pop()
numbers.remove(3)

# numbers[3] = 1.0    # only add same datatype
numbers[3] = 7

print(len(numbers))
print(type(numbers))
print(numbers)