def polinizacaoGlobal(b, g, l):
    k = {}
    k['temp'] = b['temp'] + l*(b['temp']-g['temp'])
    k['frac_1'] = b['frac_1'] + l*(b['frac_1']-g['frac_1'])
    k['frac_2'] = 1 - k['frac_1']
    return k