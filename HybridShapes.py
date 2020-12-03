from Shapes import Shape, Circle, Rectangle

class HybridShapeA(Circle, Rectangle):
    pass

class HybridShapeB(Rectangle, Circle):
    pass

hsa = HybridShapeA(6)
print(hsa)
print(hsa.calc_surface())

hsb = HybridShapeB(6)
print(hsb)
print(hsb.calc_surface())
hsb.swap_sides()
print(hsb)

