# Принцип підстановки Барбари Лісков (Liskov Substitution Principle)

class Shape:
    def area(self):
        raise NotImplementedError("Підкласи повинні перевизначати метод фігури")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

if __name__ == "__main__":
    shapes = [
        Rectangle(3, 4), 
        Square(5)         
    ]

    for shape in shapes:
        print(f"Площа фігури дорівнює: {shape.area()}")
