class Rectangle:
    # def __init__(self):
    #     self.a = 10
    #     self.b = 6

    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


r = Rectangle()
print(r.calc_surface())

r2 = Rectangle(2, 7)
print(r2)