import math

Reset = '\033[0m'
cyan = '\033[34m'


Radius = int(input("Enter the radius of the circle, the area whereof you want to calculate: "))

Area = math.pi * Radius ** 2
Area = round(Area, 2)

print(f"The area of the circle is {Red} {Area} {Reset}")