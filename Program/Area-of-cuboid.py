# 6 : WAP to calculate a Area of Cuboid.

length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

result = 2 * (length * width + width * height + height * length)

print("Area of the cuboid is:- ",result)
