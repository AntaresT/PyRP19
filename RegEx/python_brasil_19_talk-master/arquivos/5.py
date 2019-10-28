# -*- coding: utf-8 -*-
from re import findall

# Capturar o nome próprio
texto = "Meu nome é João Marcos"
# grupos ficam dentro de parenteses
# conjuntos colchetes | [^ ] -> Negação de conjunto
pattern = r"([A-Z]\w+)+"

# pattern = r".([A-Z][^ ]+)"

print(findall(pattern, texto))
