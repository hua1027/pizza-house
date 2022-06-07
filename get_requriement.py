import random
import constant

def requirement():
    a = random.randint(1, 34)
    b = a
    if a//7 != 4:
        while b//7 == a//7:
            b = random.randint(1, 34)
    if a//7 == 4:
        constant.v1 = a
    elif b//7 == 4:
        constant.v2 = b
    else:
        constant.v1 = a
        constant.v2 = b
    c = random.randint(1, 11)
    d = c
    if c // 3 != 3:
        while d // 3 == c // 3:
            d = random.randint(1, 11)
    if c // 3 == 3:
        constant.m1 = c
    elif d // 3 == 3:
        constant.m2 = d
    else:
        constant.m1 = c
        constant.m2 = d