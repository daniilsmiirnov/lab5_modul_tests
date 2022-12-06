import math
import unittest
def counting(A,B,C):
    result = []

    D=B*B-4*A*C

    if (D < 0) or (A==B==C==0):
        return result
    if (A==0):

        x6 = -math.sqrt(abs(-C/B))
        x7 = math.sqrt(abs(-C/B))
        result.append(x6)
        result.append(x7)
        return result
    t1=((-B)+ math.sqrt(D)) / (2 * A)
    t2=((-B)- math.sqrt(D)) / (2 * A)
    if (D==0):
        if t1>=0:
            x1=(-B)/(2*A)
            result.append(x1)
    if (D > 0):
            if t1>=0:
                x2 = -math.sqrt(t1)
                x3 = math.sqrt(t1)
                result.append(x2)
                result.append(x3)
            if t2 >= 0:
                x4 = -math.sqrt(t2)
                x5 = math.sqrt(t2)
                if (x4!=x2):
                    result.append(x4)
                if (x5!=x3):
                    result.append(x5)
    return result



