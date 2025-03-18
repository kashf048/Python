# letters = ["a", "b", "c"]
# for letter in enumerate(letters):   # this enumerater object will give us a tuple.
#     # print(letter)
#     # print(letter[0])
#     print(letter[0], letter[1])

letters = ["a", "b", "c"]
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)