# Constructor, which is a special method that is called when view point object.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    
point = Point(1, 2)
# print(point.x)
print(point.draw)
point.draw()