
import cmath
import math

print("quadratic equation solver")

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("there are two real roots.")
    print("first roots : {}\nsecond roots : {}".format(x1, x2))

elif delta == 0:
    x1 = (-b) / (2 * a)
    print("there is one real root :" + x1)

else:
    x1 = (-b - cmath.sqrt(delta)) / (2 * a)
    x2 = (-b + cmath.sqrt(delta)) / (2 * a)
    print("there are two complex roots.")
    print("first roots : {}\nsecond roots : {}".format(x1, x2))
