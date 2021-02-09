# 第13章のチャレンジ
# http://tinyurl.com/hz9qdh3

class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

class Square(Shape):
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        return 4 * self.side

rectangle = Rectangle(20, 50)
square = Square(29)


print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())

rectangle.what_am_i()
square.what_am_i()

class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

SABUCHAN = Rider("Kitajima Saburo")
KITASAN = Horse("KITASAN BLACK", SABUCHAN)
print(KITASAN.name)
print(KITASAN.owner.name)