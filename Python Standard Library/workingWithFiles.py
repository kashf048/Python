from pathlib import Path
from time import ctime
import shutil

# path = Path(r"D:/Stack C/All Program/Python/Python Standard Library/ecommerce/__init__.py")
source = Path(r"D:/Stack C/All Program/Python/Python Standard Library/ecommerce/__init__.py")

target = Path() / "__init__.py"

shutil.copy(source, target)

# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(path.stat())
# print(ctime(path.stat().st_ctime))

# with open("__init__.py", "r") as file:
#     ...

# print(path.read_text())
# path.write_text("...")
# path.write_bytes()