# 第21章のチャレンジ
# http://tinyurl.com/j7d7nx2

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items) -1
        return self.items[last]

    def size(self):
        return len(self.items)

a_stack = Stack()

for c in "yesterday":
    a_stack.push(c)

a_reverse = ""

while a_stack.size():
    a_reverse += a_stack.pop()

print(a_reverse)

b_stack = Stack()

for i in range(1, 6):
    b_stack.push(i)

b_reverse =  []

while b_stack.size():
    b_reverse.append(b_stack.pop())

print(b_reverse)