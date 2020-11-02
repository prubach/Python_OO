class Rectangle:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self.__a = a
        self.b = par_b

    def calc_surface(self):
        return self.__a*self.b

    @staticmethod
    def calculate_surface(par_a, par_b):
        return par_a * par_b

    def get_a(self):
        return self.__a

    def __repr__(self):
        return "Rectangle[" + str(self.__a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

r = Rectangle(5, 6)
print(r.calculate_surface(7, 8))