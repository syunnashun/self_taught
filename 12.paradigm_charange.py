# 第12章のチャレンジ
# http://tinyurl.com/gpqe62e

# 'りんご'から思い浮かぶ4つの属性を考え，インスタンス変数に持たせて，Appleクラスを定義するプログラム
# 名前，重さ，色，腐る性質をインスタンス変数に持たせる
class Apple:
    def __init__(self, n, w, c):
        self.name = n
        self.weight = w
        self.color = c
        self.mold = 0

    def rot(self, days, temp):
        self.mold = days * temp

    def sweetness(self):
        return 100 / self.weight

# どうやら，変数の型はこの処理で決まるようだ
ap1 = Apple("Orin", 50, "red")
print(ap1.name)
print(ap1.weight)
print(ap1.color)

# 関数的な使い方だね
ap1.rot(14, 3)
print(ap1.mold)

print(ap1.sweetness())

# 円を表すクラスに，面積を計算して返すメソッドを持たせ，結果を出力するプログラム

import math

class Circle:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return math.pi * self.radius * self.radius

circle = Circle(5)
print(circle.area())

# 三角形の面積を返すプログラム

class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h

    def area(self):
        return self.bottom * self.height / 2

    def change_size(self, b, h):
        self.bottom = b
        self.height = h

triangle = Triangle(7, 4)
print(triangle.area())
triangle.change_size(10, 5)
print(triangle.area())

# 六角形を表すクラスを定義し，外周の長さを計算して返すメソッドを呼び出し，結果を出力するプログラム

class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())