


def area(l,w):
    return l*w 

    



def circum(rad):
    return 2* 3.14* rad

print("input Radius of Circle: ", end="")
r = float (input())

c = circum(r)
print("\nCircumference = {: .2f}". format(c))