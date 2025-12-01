import math

class Shape:
    def area(self): raise NotImplementedError
    def perimeter(self): raise NotImplementedError
    def vertices(self): return 0   

class Triangle(Shape):
    def __init__(self, x1,y1,x2,y2,x3,y3):
        self.a = (x1,y1); self.b = (x2,y2); self.c = (x3,y3)
    def area(self):
        x1,y1 = self.a; x2,y2 = self.b; x3,y3 = self.c
        return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
    def perimeter(self):
        d = lambda p,q: math.hypot(p[0]-q[0], p[1]-q[1])
        return d(self.a,self.b)+d(self.b,self.c)+d(self.c,self.a)
    def vertices(self): return 3

class Rectangle(Shape):
    def __init__(self, x1,y1,x2,y2):
        self.w = abs(x2-x1); self.h = abs(y2-y1)
    def area(self): return self.w*self.h
    def perimeter(self): return 2*(self.w+self.h)
    def vertices(self): return 4

class Circle(Shape):
    def __init__(self, cx,cy,r):
        self.r = r
    def area(self): return math.pi*self.r*self.r
    def perimeter(self): return 2*math.pi*self.r

def parse_shape(line):
    t, *a = line.split()
    a = list(map(float, a))
    if t == "triangle":   return Triangle(*a)
    if t == "rectangle":  return Rectangle(*a)
    if t == "circle":     return Circle(*a)
    raise ValueError("Неизвестная фигура")

shapes = []
print("Введите фигуры (triangle/rectangle/circle ...) или команду: area / perimeter / vertices / quit")

while True:
    line = input("> ").strip()
    if not line: continue

    if line == "quit":
        break

    if line in ("area","perimeter","vertices"):
        if not shapes:
            print("Нет фигур")
            continue

        if line == "area":
            print("Total area:", sum(s.area() for s in shapes))
        elif line == "perimeter":
            print("Total perimeter:", sum(s.perimeter() for s in shapes))
        elif line == "vertices":
            print("Total vertices:", sum(s.vertices() for s in shapes))
        continue

    try:
        fig = parse_shape(line)
        shapes.append(fig)
        print("Фигура добавлена.")
    except Exception as e:
        print("Ошибка:", e)