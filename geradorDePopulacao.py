import random


def Populacao_azeotropos(temp_min, temp_max, frac_min, frac_max, n):
    populacao = {}
    for i in range(0, n, 1):
        frac_1 = random.uniform(frac_min, frac_max)
        frac_2 = 1 - frac_1
        populacao[i] = {'temp': random.uniform(temp_min, temp_max), 
                        'frac_1': frac_1, 
                        'frac_2': frac_2}
    return populacao