class Rectangle:
    def __init__(self, p_a=5, b=10):
        self.a = p_a
        self.b = b

    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a*self.b

r = Rectangle(p_a=4, b=8)
#r.set_params(4, 5)
print(r.calc_surface())
print(r)