old = ['a', 'b', 'a', 'c', 'b', 'a']

# First
# new = list(set(old))

# Second
# new = []
# for item in old:
#     if item not in new:
#         new.append(item)


# Third
new = list(dict.fromkeys(old).keys())

print(new)