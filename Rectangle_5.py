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


def calculate_surface(par_a, par_b):
    return par_a*par_b


r = Rectangle(5, 6)

s1 = "abcd"
s2 = s1
s1 = s1.lower()

# s1 = 333
# s2 = s1
# s1 = s1 + 2

print(id(s1))
print(id(s2))


print(r.calculate_surface(7, 8))

print(calculate_surface(7, 8))
