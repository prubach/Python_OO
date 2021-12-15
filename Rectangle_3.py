class Rectangle:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self.__a = a
        self.b = par_b

    def calc_surface(self):
        return self.__a*self.b

    def set_a(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def __repr__(self):
        return "Rectangle[" + str(self.__a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

r = Rectangle(5, 6)
r.a = 10
r.__a = 8
print(r)
r.set_a(11)
print(r)
print(r.calc_surface())
print('__a in r is: ' + str(r.get_a()))
print('r.__a in is: ' + str(r.__a))
print('r.a in is: ' + str(r.a))
