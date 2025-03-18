def increment(number: int, by: int = 1) -> tuple:
# def increment(number, by):
    return (number, number + by)


print(increment(2, by=3))  # by=3 keyword argument code more readable
print(increment(2))