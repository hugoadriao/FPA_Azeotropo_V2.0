from misturas import Mistura


def Tij(nome, i, j, T, R):
    if (i == j):
        return 0
    else:
        t = (Mistura(nome, i, j)) / (R*(T-273.15))
        return t