from math import log
from elementos import Elemento
from psat import Psat
from misturas import Mistura
from nrtl import Nrtl
from gera_teste import Catch_nome


def Azeo(indv):
    nome1, nome2, p = Catch_nome()
    nome_elem = [nome1, nome2]
    atm = p*101.325
    n = 2
    elem = [0]
    r = []
    T = indv['temp']
    for i in nome_elem:
        elem.append(Elemento(i))
    mistura = nome_elem[0]+'-'+nome_elem[1]
    for i in range(1, n+1, 1):
        r.append(
            log(atm) - log(Psat(T, elem[i])) - log(Nrtl(mistura, indv, T, n, i)))
    r1 = r[0]
    r2 = r[1]
    return pow(r1, 2) + pow(r2, 2) + pow(((indv['frac_1']+indv['frac_2'])-1), 2)