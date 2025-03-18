def save_user(**user):
    print(type(user))
    # print(user)
    # print(user["id"])
    print(user["name"])


save_user(id=1, name="admin")


def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Average: ", sum / len(numbers))


average(2, 4, 5, 10)