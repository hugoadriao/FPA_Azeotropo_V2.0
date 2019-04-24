from gamma import Gamma_simpson as Gamma
from math import sin, pi


def Levy(s0):
    lbm = 1.5
    s = 1+1e-5*s0
    l = (lbm*Gamma(lbm)*sin((pi*lbm)/2))/(pi*pow(s, 1+lbm))
    return l