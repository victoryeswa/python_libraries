import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)
        else:
            x = self.x + other
            y = self.y + other




    def plot(self):
        plt.scatter(self.x, self.y)

a = Point(1, 1)
b = Point(2, 2)
c = a + b
d = a +5

print(d.x, d.y)
print(c.y, c.x)


    

