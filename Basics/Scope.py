message = "a"       # global variable
def greet():
    global message
    message = "b"   # local variable


greet()
print(message)