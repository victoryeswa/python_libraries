import turtle

class Polygon:
    def __init__(self, sides, name, size, color = 'black', line_thickness=2):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles =(self.sides-2)*180
        self.angle = self.interior_angles/self.sides
    

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(self.angle)
        turtle.done()


def draw_function(sides, size, angle, line_thickness, color):
    turtle.color(color)
    turtle.pensize(self.line_thickness)
    for i in range(self.size):
        turtle.forward(self.size)
        turtle.right(180-self.angle)
    turtle.done()





square = Polygon(4, 'Square', 100)
pentagon = Polygon(5, 'Pentagon', 100)

print(square.sides)
print(square.name)
print(square.interior_angles)
print(square.angle)

print(pentagon.sides)
print(pentagon.name)

square.draw()

hexagon = Polygon(6, 'Hexagon', 40)
pentagon.draw()