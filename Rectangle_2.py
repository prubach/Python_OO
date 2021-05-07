class Rectangle:
    def __init__(self, a=10, b=6):
         self.set_params(a, b)

# def __init__(self):
#      self.a = 5
#      self.b = 8

    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


r = Rectangle(b=8)
r.a = 50
print(r.calc_surface())
# destroy r
#del r

r2 = Rectangle(2, 7)
print(r2)