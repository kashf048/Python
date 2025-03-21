from pathlib import Path

path = Path(r"D:/Stack C/All Program/Python/Python Standard Library/ecommerce/__init__.py")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# print(path.iterdir())
# for p in path.iterdir():
#     print(p)

# paths = [p for p in path.iterdir()]
# print(paths)

# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)

py_files = [p for p in path.glob("*.py")]
print(py_files)