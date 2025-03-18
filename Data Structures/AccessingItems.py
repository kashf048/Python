letters = ["a", "b", "c", "d"]

print(letters[0])
print(letters[-1])

letters[0] = "A"
print(letters)
print(letters[0:3])
print(letters[:3])
print(letters[0:])
print(letters[:])   # copy list

letters2 = list(range(20))
print(letters2[::2])   # every 2nd or 3rd element in the orignal list
print(letters2[::3]) 
print(letters2[::-1])   # reverse the orignal list

