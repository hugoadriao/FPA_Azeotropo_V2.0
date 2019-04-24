from azeo import Azeo
from polinizacaoCruzada import polinizacaoGlobal
from polinizacaoDireta import polinizacaoLocal
from levy import Levy
import random


contador_funcao = 0


def Fpa(n, dic, valor_esperado, saida_nome):
    # armazena o numero de invocacoes feitas da funcao problema 
    global contador_funcao
    # variavel temporaria para o armazenamento do numero de vezes que a funcao problema e utilizada no codigo
    contador_funcao = 0
    # variavel de tolerancia
    tol = pow(10, -8)
    # variavel utilizada para setar a probabilidade de polinizacao global
    prob = 0.8
    # variavel utilizada para armazenar os individous
    populacao = dic
    # variavel utilizada para armazenar os novos individous
    nova_populacao = {}
    # variavel utilizada para armazenar o melhor individou
    g = {}
    # variavel utilizada para armazenar as aptidoes do individuos
    aptd = []
    # limites
    temp_min = 283
    temp_max = 473
    frac_min = 0
    frac_max = 1
    # calculo de aptidao, os valores de cada individou e utilizado na funcao
    for i in populacao.values():
        valor = Azeo(i)
        aptd.append(valor)
        contador_funcao += 1
    # atribui o primeiro elemento para futuro teste
    pivot = aptd[0]
    g = populacao[0]
    # verifica qual individou tem a melhor aptidao
    for i in populacao.keys():
        # checando populacao
        if pivot > aptd[i]:
            pivot = aptd[i]
            # armazena o individou com melhor aptidao
            g = populacao[i]
    # teste de probabilidade de ocorrer polinizacao global
    # Polinizacao global
    if (random.uniform(0, 1) <= prob):
        l = Levy(n)
        for i in populacao.keys():
            nova_populacao[i] = polinizacaoGlobal(populacao[i], g, l)
    # Polinizacao local
    else:
        count = len(dic)-1
        a = random.randint(0, count)
        b = random.randint(0, count)
        while a == b:
            b = random.randint(0, count)
        b_a1 = populacao[a]
        b_a2 = populacao[b]
        for i in populacao.keys():
            nova_populacao[i] = polinizacaoLocal(populacao[i], b_a1, b_a2)
    
    # Teste dos limites
    for i in nova_populacao.keys():
        if (nova_populacao[i]['frac_1'] < frac_min):
            nova_populacao[i]['frac_1'] = frac_min+(0.3*random.uniform(0, 1))
            nova_populacao[i]['frac_2'] = 1 - nova_populacao[i]['frac_1']

        if (nova_populacao[i]['frac_1'] > frac_max):
            nova_populacao[i]['frac_1'] = frac_max-(0.3*random.uniform(0, 1))
            nova_populacao[i]['frac_2'] = 1 - nova_populacao[i]['frac_1']

        if (nova_populacao[i]['temp'] < temp_min):
            nova_populacao[i]['temp'] = temp_min+(0.3*random.uniform(0, 1))

        if (nova_populacao[i]['temp'] > temp_max):
            nova_populacao[i]['temp'] = temp_max-(0.3*random.uniform(0, 1))

    # checa e organiza os novos valores
    for i in populacao.keys():
        old_indv = Azeo(populacao[i])
        contador_funcao += 1
        new_indv = Azeo(nova_populacao[i])
        contador_funcao += 1
        if new_indv < old_indv:
            populacao[i] = nova_populacao[i]
    n_aptd = []
    # procura pelo novo melhor individuo
    for i in populacao.values():
        n_aptd.append(Azeo(i))
        contador_funcao += 1
    pivot = n_aptd[0]
    g = populacao[0]
    for i in populacao.keys():
        # checando populacao
        if pivot > n_aptd[i]:
            pivot = n_aptd[i]
            # armazena o individou com melhor aptidao
            g = populacao[i]
    contador_funcao += 1
    if abs(valor_esperado - pivot) <= tol:
        with open(f'result/{saida_nome}.txt', 'a') as f:
            # numero de iteracoes: n
            # numero de vezes que a funcao foi utilizada: contador_funcao
            # solucao: g
            # aptidao: pivot
            f.write(f'\n{n};{contador_funcao};{g};{pivot}')
            contador_funcao = 0
        return True
    else:
        return populacao