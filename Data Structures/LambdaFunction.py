items = [
    ("Product1", 10), 
    ("Product2", 9), 
    ("Product3", 12), 
]

# def sort_item(item):
#     return item[1]

# items.sort(key=lambda parameter:expression)
items.sort(key=lambda item:item[1]) # lambda function or anonymous function and remove sort_item function
print(items)