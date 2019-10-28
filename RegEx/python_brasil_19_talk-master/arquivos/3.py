# -*- coding: utf-8 -*-
from re import findall
# dentro da chame é o quantificador
pattern = r'[01]{2}'

texto = """
11
10
01
11
"""

print(findall(pattern, texto))
# intervalo aberto com o a virgula
# colchete usado para OU [01] ou 1 ou 0
# + tambem pode ser quantificador (uma ou mais vezes)
# * 0 ou mais vezes
# ? 0 ou 1 vez
pattern = r'[01]{2,}'
#pattern = r"1+"

texto = """
111
110
101
100
"""

print(findall(pattern, texto))
