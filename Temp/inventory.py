inv = ["Sword", None, None]
# inv = ["Sword", "Shield", "Gem"]
# inv = [None, None, None]

if all(inv):
    print("Inventory full!")
elif any(inv):
    print("Inventory has items!")
else:
    print("Inventory empty!")