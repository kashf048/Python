numbers = [1, 2, 3, 4, 4, 4, 4, 9]

# first, second, third = numbers  # 2 in 1 but is efficient
# first, second = numbers 
# first, second, *other = numbers 
first, *other, last = numbers 
print(first, last)
print(other)

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]