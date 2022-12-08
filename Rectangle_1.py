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

r1 = Rectangle()
r1.set_params(4, 5)
print(r1.calc_surface())
print('R1: {}'.format(r1))
#
r2 = Rectangle()
r2.set_params(6, 7)
print(r2.calc_surface())
print('R2: {}'.format(r2))

# r3 = r1
# print('R3: {}'.format(r3))
# #
# from copy import copy
# r4 = copy(r2)
# print('R4: {}'.format(r4))
# print('R1=R3: {}'.format(r1==r3))
# print('R2=R4: {}'.format(r2==r4))
# print('R2 compare R4: {}'.format(r2.compare(r4)))
# print('R1=R3: {}'.format(r1==r3))
# print('R1 compare R3: {}'.format(r1.compare(r3)))
#
# print('R4: {}'.format(r4))
# #
# lr1_list = [r1, r2, r3, r4]
# print(f'LR1_list:{lr1_list}')
# lr2_list = lr1_list
# print(f'LR2_list:{lr2_list}')
# lr3_list = lr1_list.copy()
# print('r3_list:')
# print(lr3_list)
# lr1_list[0].set_params(9, 8)
# print(f'LR1_list:{lr1_list}')
# print(f'LR2_list:{lr2_list}')
# print(f'LR3_list:{lr3_list}')
# from copy import deepcopy
# lr4_list = deepcopy(lr1_list)
# print(f'LR4_list:{lr4_list}')
# lr4_list[0].set_params(10, 15)
# print(f'LR1_list:{lr1_list}')
# print(f'LR2_list:{lr2_list}')
# print(f'LR3_list:{lr3_list}')
# print(f'LR4_list:{lr4_list}')

# print('changing params')
#r2.set_params(3, 2)
#
# #del r4_list
# print(f'R_list:{r_list}')
# print(f'R2_list:{r2_list}')
# print(f'R3_list:{r3_list}')
# print(f'R4_list:{r4_list}')
