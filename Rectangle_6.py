class Rectangle:
    num_rect = 0
    def __init__(self, a=10, b=6):
        self.set_params(a, b)
        Rectangle.num_rect += 1

    def set_params(self, a, par_b):
        self.__a = a
        self.b = par_b

    @classmethod
    def count(cls):
        return cls.num_rect

    def calc_surface(self):
        return self.__a*self.b

    def get_a(self):
        return self.__a

    def __repr__(self):
        return "Rectangle[" + str(self.__a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

r = Rectangle(5, 6)

print("Num of rect: " + str(r.count()))

r2 = Rectangle(4, 8)

print("Num of rect: " + str(r.count()))
