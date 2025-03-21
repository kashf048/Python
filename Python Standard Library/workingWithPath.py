from pathlib import Path

# Path(r"C:\Program Files\Microsoft")     # window
# Path("usr/locla/bin")       # Mac
# Path()
# Path("ecommerce/__init__.py")
# Path.home()
path = Path() / "ecommerce" / "__init__.py"
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
print(path)
print(path.absolute)
print(path.absolute())
path = path.with_suffix(".txt")
print(path)