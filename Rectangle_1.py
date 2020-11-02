class Rectangle:
    def set_params(self, a, b):
        self.a = a
        self.b = b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

