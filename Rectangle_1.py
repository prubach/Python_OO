class Rectangle:
    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

r = Rectangle()
r.set_params(4, 5)
area = r.calc_surface()
print(r)
print('area of r is: ' + str(area))
r2 = Rectangle()
r2.set_params(6, 7)
print(r2)
r3 = r
r3.set_params(2,3)
print(r3)
#
print()
x = [ r, r2, r3 ]
#
#y = x.copy()
from copy import deepcopy
y = deepcopy(x)
print(x)
print('after making a copy')
print(y)
x[1].set_params(8, 9)
print('after assigning 8 by 9 to r2')
print(x)
print(y)
#
