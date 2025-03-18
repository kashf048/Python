try:
    file = open("Exception.py")
    age = int(input("Age: "))
    xfactor = 10 / age   
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()