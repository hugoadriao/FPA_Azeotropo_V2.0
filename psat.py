from math import pow


def A(i):
    a = {
        0: 7.63130,  # acetone
        2: 6.87987,  # benzene
        3: 7.44777,  # cloroform
        4: 8.11220,  # ethanol
        6: 7.03295,  # hexafluorobenzene
        8: 8.08097,  # methanol
        12: 7.06356,  # methyl
        13: 8.87829,  # i-propanol
        14: 7.74416,  # n-propanol
        15: 8.07131  # water

    }
    return a[i]


def B(i):
    b = {
        0: 1566.690,  # acetone
        2: 1196.760,  # benzene
        3: 1488.990,  # cloroform
        4: 1592.864,  # ethanol
        6: 1227.984,  # hexafluorobenzene
        8: 1582.271,  # methanol
        12: 1261.340,  # methyl
        13: 2010.330,  # i-propanol
        14: 1437.686,  # n-propanol
        15: 1730.630  # water
    }
    return b[i]


def C(i):
    c = {
        0: 273.419,  # acetone
        2: 219.161,  # benzene
        3: 264.915,  # cloroform
        4: 226.184,  # ethanol
        6: 215.491,  # hexafluorobenzene
        8: 239.726,  # methanol
        12: 221.969,  # methyl
        13: 252.636,  # i-propanol
        14: 198.463,  # n-propanol
        15: 233.426  # water
    }
    return c[i]


def Psat(T, i):
    r = 0.133322387415*pow(10, (A(i)-(B(i)/(C(i)+(T-273.15)))))
    return r