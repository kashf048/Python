# values = []
# for x in range(5):
#     values.append(x * 2)

# [expression for item in items]
# values = {x * 2 for x in range(5)}

values = {}
for x in range(5):
    values[x] = x * 2

# values = {x: x * 2 for x in range(5)}
values = (x * 2 for x in range(5))
# {1, 2, 3, 4}
# {1: "a", 2: "b"}

print(values)