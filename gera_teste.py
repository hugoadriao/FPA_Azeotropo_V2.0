nome1 = ''
nome2 = ''
atm = 0


def Gera_mistura(nome):
    global nome1, nome2, atm
    mistura = {
        'AC': {'nome1': 'acetone', 'nome2': 'cloroform', 'atm': 1},
        'AC2': {'nome1': 'acetone', 'nome2': 'cloroform', 'atm': 15.8},
        'AM2': {'nome1': 'acetone', 'nome2': 'methanol', 'atm': 15.8},
        'AM': {'nome1': 'acetone', 'nome2': 'methanol', 'atm': 1},
        'BH': {'nome1': 'benzene', 'nome2': 'hexafluorobenzene', 'atm': 0.2},
        'BIP': {'nome1': 'benzene', 'nome2': 'ipropanol', 'atm': 1},
        'BNP': {'nome1': 'benzene', 'nome2': 'npropanol', 'atm': 1},
        'CM': {'nome1': 'cloroform', 'nome2': 'methanol', 'atm': 1},
        'CM2': {'nome1': 'cloroform', 'nome2': 'methanol', 'atm': 15.8},
        'CE': {'nome1': 'cloroform', 'nome2': 'ethanol', 'atm': 1},
        'EB': {'nome1': 'ethanol', 'nome2': 'benzene', 'atm': 1},
        'EMY': {'nome1': 'ethanol', 'nome2': 'methyl', 'atm': 1},
        'EW': {'nome1': 'ethanol', 'nome2': 'water', 'atm': 1},
        'MYW': {'nome1': 'methyl', 'nome2': 'water', 'atm': 1},
        'MB': {'nome1': 'methanol', 'nome2': 'benzene', 'atm': 1}

    }
    nome1 = mistura[nome]['nome1']
    nome2 = mistura[nome]['nome2']
    atm = mistura[nome]['atm']


def Catch_nome():
    return nome1, nome2, atm