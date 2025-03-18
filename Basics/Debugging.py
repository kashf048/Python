def multiply(*list):
    total = 1
     for number in list:
        total *= number
    return total

print("start")
print(multiply(2, 3, 4, 5))
print("finish")