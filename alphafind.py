import math


def alpha_1(counter):
    return math.sin(counter)/counter


def alpha_2(counter):
    return math.exp(-counter)*counter**2


#c = [abs(alpha_2(x)) for x in range(1, 10000)]
#print(c)
