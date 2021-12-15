class Rectangle:
    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a*self.b

    def compare(self, other_r):
        if self.a==other_r.a and self.b==other_r.b:
            return True
        else:
            return False

    def __repr__(self):
        return 'Rectangle[{} by {} at {}]'.format(self.a, self.b, hex(id(self)))
    #def __str__(self):
    #    return 'Rectangle[{} by {} at {}]'.format(self.a, self.b, hex(id(self)))

r = Rectangle()
r.set_params(4, 5)
print(r.calc_surface())
print('R: {}'.format(r))
#
r2 = Rectangle()
r2.set_params(6, 7)
print(r2.calc_surface())
print('R2: {}'.format(r2))

r3 = r
print('R3: {}'.format(r3))

from copy import copy
r4 = copy(r2)
print('R2=R4: {}'.format(r2==r4))
print('R2 compare R4: {}'.format(r2.compare(r4)))
print('R1=R3: {}'.format(r==r3))
print('R1 compare R3: {}'.format(r.compare(r3)))

print('R4: {}'.format(r4))
#
r_list = [r, r2, r3, r4]
print('r_list:')
print(r_list)
r2_list = r_list
print('r2_list:')
print(r2_list)
r3_list = r_list.copy()
print('r3_list:')
r_list[0].set_params(9, 8)
print(r3_list)
print(r2_list)
print(r)
from copy import deepcopy
r4_list = deepcopy(r_list)
r4_list[0].set_params(10, 15)
print('r4_list:')
print(r4_list)
print('r2_list:')
print(r2_list)

#
#
# print('changing params')
# r2.set_params(8, 9)
# print(r_list)
# print(r2_list)
# print('r4_list:')
# print(r4_list)
#
# #del r4_list
# #print('r4_list:')
# #print(r4_list)
