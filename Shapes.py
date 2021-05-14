class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


class Sphere(Circle):
    def calc_volume(self):
        return 4/3*math.pi*self._a**3

    def calc_surface(self):
        return 4*super().calc_surface()


a = None

r = Rectangle(5, 6)
print(r)
#r._a = 600
print(r.calc_surface())
r.swap_sides()
r_desc = str(r)
print(r_desc)

c = Circle(7)
c_desc = str(c)
print(c_desc)
print(c.calc_surface())
s = Sphere(8)
print(s)
print('s volume: ')
print(s.calc_volume())
print('s surface:')
print(s.calc_surface())

shape_list = [r, c, s]
print()
print('--------------------')
for sh in shape_list:
    print(sh.__class__.__name__)
    sh.set_params(10, 15)
    print(sh.calc_surface())