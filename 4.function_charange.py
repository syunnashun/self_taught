# 第4章のチャレンジ
# http://tinyurl.com/hkzgqrv

def f():
    x = input("type a number:")
    x = int(x)
    return x ** 2
result_x = f()
print(result_x)

def g():
    y = "I love softeni!"
    print(y)
g()

def h(a, b, c, d=7, e=2):
    return a + b * c - d / 2
result_h = h(1, 4, 9)
print(result_h)

def devide(x):
    return x / 2

def multiply(x):
    return x * 4

y = devide(4)
z = multiply(y)
print(z)

def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the message to a float.")
p = convert("77.77")
print(p)