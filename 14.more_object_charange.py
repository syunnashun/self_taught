# 第14章のチャレンジ
# http://tinyurl.com/j9qjnep

class Shape:
    def what_am_I(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)
    
    def calculate_perimeter(self):
        return self.side * 4

    def what_am_I(self):
        super().what_am_I() # [super().親クラスのメソッド]で親クラスのメソッドを呼び出せる
        print("I am a shape.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

s1 = Square(100)
s2 = Square(200)
s3 = Square(777)
print(Square.square_list)
print(s1) # クラス変数の扱い

def judge():
    para1 = input("Input first parameter: ")
    para2 = input("Input second parameter: ")
    print(para1 is para2)

judge()