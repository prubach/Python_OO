class Shape:
    def __init__(self, a=1, b=1):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def get_b(self):
        return self.b

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def calc_perimeter(self):
        return 2*self._a+2*self.b

import math

class Circle(Shape):
    def __init__(self, a):
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi*self._a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


class HybridShape(Rectangle, Circle):
    pass

class HybridShapeB(Circle, Rectangle):
    pass


r = Rectangle(5, 7)
r._a = 325
print(r)
print(r.calc_surface())

s = Circle(50)
print(s)
print(s.calc_surface())

hs = HybridShape(5)
print(hs)
print(hs.calc_surface())
print(hs.calc_perimeter())

hsb = HybridShapeB(10)
print(hsb)
print(hsb.calc_surface())
print(hsb.calc_perimeter())
