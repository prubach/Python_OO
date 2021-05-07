class Rectangle:
    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return 'Rectangle[{} by {}] at {}]'.format(self.a, self.b, hex(id(self)))

r = Rectangle()
r.set_params(4, 5)
print(r.calc_surface())
print(r)

r2 = Rectangle()
r2.set_params(4, 5)
print(r2.calc_surface())
print(r2)
from copy import copy
r3 = copy(r2)
print(r3)

r_list = [r, r2, r3]
print('r_list:')
print(r_list)
r2_list = r_list
r3_list = r_list.copy()
from copy import deepcopy
r4_list = deepcopy(r_list)
print('r2_list:')
print(r2_list)
print('r4_list:')
print(r4_list)


print('changing params')
r2.set_params(8, 9)
print(r_list)
print(r2_list)
print('r4_list:')
print(r4_list)

#del r4_list
#print('r4_list:')
#print(r4_list)
