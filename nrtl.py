from math import exp
from tij import Tij
from gij import Gij
from misturas import Mistura, Alpha

R = 8.314


def Nrtl(mistura, indv, T, n, i):
    global R
    sum1 = sum3 = sum4 = sum5 = sum6 = 0
    aux1 = aux2 = aux3 = 0
    alpha = Alpha(mistura)

    # print(indv)

    for j in range(1, n+1, 1):
        # reseta as variaveis para uma nova iteracao de J
        sum1 = sum3 = 0
        for k in range(1, n+1, 1):
            xk = indv[f'frac_{k}']
            tkj = Tij(mistura, k, j, T, R)
            gkj = Gij(tkj, k, j, alpha)
            sum1 += xk * gkj
            sum3 += xk*tkj*gkj
        xj = indv[f'frac_{j}']
        tij = Tij(mistura, i, j, T, R)
        gij = Gij(tij, i, j, alpha)
        aux1 = (xj*gij)/sum1
        aux2 = tij - (sum3/sum1)
        sum4 += aux1*aux2
        # -------------------------------------------
    for j in range(1, n+1, 1):
        xj = indv[f'frac_{j}']
        tji = Tij(mistura, j, i, T, R)
        gji = Gij(tji, j, i, alpha)
        sum5 += xj*tji*gji
    for k in range(1, n+1, 1):
        xk = indv[f'frac_{k}']
        tki = Tij(mistura, k, i, T, R)
        gki = Gij(tki, k, i, alpha)
        sum6 += xk * gki
    aux3 = sum5/sum6
    r = exp(aux3+sum4)
    return r