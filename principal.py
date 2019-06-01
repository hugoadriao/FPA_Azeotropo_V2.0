from fpa import Fpa
from geradorDePopulacao import Populacao_azeotropos as populacaoInicial
from gera_teste import Gera_mistura

print('Informe o nome da mistura conforme um dos exemplos a baixo:')
print("""
    AC: Acetone-Cloroform 1Atm
    AC2: Acetone-Cloroform 15.8Atm
    AM: Acetone-Methanol 1Atm
    AM2: Acetone-Methanol 15.8 Atm
    BH: Benzene-Hexafluorobenzene 0.2 Atm
    BIp: Benzene-I-propanol 1Atm
    BNp: Benzene-N-propanol 1Atm
    CM: Cloroform-Methanol 1Atm
    CM2: Cloroform-Methanol 15.8Atm
    CE: Cloroform-Ethanol 1Atm
    EB: Ethanol-Benzene 1Atm
    EMy: Ethanol-Methyl 1Atm
    EW: Ethanol-Water 1Atm
    MyW: Methyl-Water 1Atm
    MB: Methanol-Benzene 1Atm""")
nome = input()
v_esp = 0
Gera_mistura(nome.upper())
temp_min = 283
temp_max = 473
frac_min = 0
frac_max = 1
n = 20
populacao = populacaoInicial(temp_min, temp_max, frac_min, frac_max, n)
saida = input('nome do arquivo de resultados\n')
result = Fpa(0, populacao, v_esp, saida)
count = 1
while result != True:
    result = Fpa(count, result, v_esp, saida)