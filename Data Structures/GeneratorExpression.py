from sys import getsizeof

# values = [x * 2 for x in range(10)]
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
# print(len(values))  # generator has no length
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))
print(len(values))
# print(values)
# for x in values:
#     print(x)