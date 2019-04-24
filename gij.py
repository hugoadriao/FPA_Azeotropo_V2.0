from math import exp


def Gij(tij, i, j, alpha):
    if(i == j):
        return 1
    else:
        gij = exp(-alpha*tij)
        return gij