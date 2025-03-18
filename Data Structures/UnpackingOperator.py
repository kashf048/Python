numbers = [1, 2, 3]
# print(...numbers)     this is use JavaScript but same result
print(*numbers)
print(1, 2, 3)

values = list(range(5))
values = [*range(5), *"Hello"]
print(values)


first = {"x": 1}
second = {"x": 10, "y": 20}
combined = {**first, **second, "z": 1}
print(combined)