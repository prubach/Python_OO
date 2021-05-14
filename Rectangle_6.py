class Rectangle:
    num_rect = 0
    def __init__(self, a=10, b=6):
        self.set_params(a, b)
        Rectangle.num_rect += 1

    @classmethod
    def count(cls):
        return cls.num_rect

    def set_params(self, a, par_b):
        self.__a = a
        self.b = par_b

    def calc_surface(self):
        return self.__a*self.b

    def get_a(self):
        return self.__a

    def __repr__(self):
        return "Rectangle[" + str(self.__a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

    def __del__(self):
        Rectangle.num_rect -= 1
        print('Destroying rectangle, left {} rectangles'.format(Rectangle.num_rect))

#
class RectangleFactory:
    def new_rect(self, a, b):
        return Rectangle(a, b)

r = Rectangle(5, 6)
print(r.count())
r2 = Rectangle(45, 3)
print(r2.count())
print(r.count())
rf = RectangleFactory()
r3 = rf.new_rect(7, 78)
print(r.count())
# print(r2.count())
del r
print(Rectangle.num_rect)