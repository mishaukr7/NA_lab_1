import math


def alpha_1(counter):
    alpha = math.sin(counter)/counter
    if abs(alpha) > 0.1:
        alpha = alpha / 100
    return alpha


def alpha_2(iter, n):
    return math.log(iter)/n


