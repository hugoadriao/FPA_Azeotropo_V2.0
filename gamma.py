# Criacao da funcao que funciona como f(x)
def func(x, t):
    from math import exp
    f = float((pow(x, t))*exp(-x))  # Gamma a = 0 V
    return f


# Criacao do algoritmo
def Gamma_simpson(t):
    t = t
    a = 0
    b = 1000
    n = 1000
    h = (b-a)/n
    x = []
    # Definicao do primeiro primeiro ponto depois de a
    pontoMedio = a+h
    # Lista "geral" de itens
    x.append(pontoMedio)
    # Lista de itens em posicoes impares
    x_impar = []
    # Lista de itens em posicoes pares
    x_par = []
    # somatorio da lista de itens pares na funcao
    soma_par = 0
    # somatorio da lista de itens impares na funcao
    soma_impar = 0
    # Resultado da integral numérica
    resultado = 0
    count = 0
    # Insere os itens na lista geral
    for i in range(1, n-1, 1):
        x.append(x[i-1]+h)
    # Insere os itens nas posicoes impares na lista de itens impares
    for i in range(0, n-1, 2):
        x_impar.append(x[i])
        soma_impar += func(x_impar[count], t)
        count += 1
    count = 0
    # Insere os itens nas posicoes pares na lista de itens pares
    for i in range(1, n-1, 2):
        x_par.append(x[i])
        soma_par += func(x_par[count], t)
        count += 1
    # Formula
    resultado = (h/3)*(func(a, t)+2*(soma_par)+4*(soma_impar)+func(b, t))
    return resultado