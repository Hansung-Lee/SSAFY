import a
print(a.square(2))
print(a.cube(2))
print(dir(a))


from a import square, cube
print(square(2))
print(cube(2))


from a import square as aa
from a import cube as bb
print(aa(2))
print(bb(2))