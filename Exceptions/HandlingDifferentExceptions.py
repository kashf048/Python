try:
    age = int(input("Age: "))
    xfactor = 10 / age      # pass 0
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
# except ZeroDivisionError:
#     # print("Age cannot be 0.")
#     print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")