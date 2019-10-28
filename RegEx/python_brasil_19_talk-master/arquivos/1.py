# -*- coding: utf-8 -*-
import re

# Ver todas as funções e constantes
# print(dir(re))

# findal sempre retorna uma lista com string do pattern que foi encontrado
from re import findall

print(re.findall("f", "fff"))

result = re.findall("xu", "xu")

print(type(result), len(result))
print(result)

result = re.findall("xu", "xuxu")

print(type(result), len(result))
print(result)

# Como é feita a leitura?
# ele nao volta, le somente 1 - 'ff' | faz a leitura e descarta
print(re.findall("ff", "fff"))
