class Rectangle:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a*self.b

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Rectangle(new_a, new_b)

    def __str__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

    def __lt__(self, other):
        this_area = self.calc_surface()
        other_area = other.calc_surface()
        return this_area < other_area


class Square:
    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a * self.b


r1 = Rectangle(2, 3)
r2 = Rectangle(5, 6)

#q = r2 < r1
#print('is r2 < r1: ' + str(q))

r3 = r1 + r2
print(r3)
# s = Square()
# s.set_params(10, 10)
#
# r4 = r1 + s
# print(r4)
#
# q = s < r1
# print('is s < r1: ' + str(q))
#
#
# #print(r1)
# #print(r2)
#
# #print(r3)
#
