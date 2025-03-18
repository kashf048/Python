names = ["Kashf", "Mansoor", "Abdullah"]
found = False
for name in names:
    if name.startswith("M"):
        print("Found")
        found = True
        break
if not found:
    print("Not found")



for name in names:  # 2 in 1 but this more clean
    if name.startswith("M"):
        print("Found")
        break
else:
    print("Not found")