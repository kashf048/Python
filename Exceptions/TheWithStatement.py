try:
    with open("Exception.py") as file:
        print("File opened.")

    age = int(input("Age: "))
    xfactor = 10 / age   
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")