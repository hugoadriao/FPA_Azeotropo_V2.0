import random


def polinizacaoLocal(b, b_a1, b_a2):
    k = {}
    k['temp'] = b['temp'] + ((random.uniform(0, 1)) *
                             (b_a1['temp']-b_a2['temp']))
    k['frac_1'] = b['frac_1'] + \
        ((random.uniform(0, 1))*(b_a1['frac_1']-b_a2['frac_1']))
    k['frac_2'] = 1 - k['frac_1']
    return k