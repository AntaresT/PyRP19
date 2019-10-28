from re import findall
# r -> usado pra "fazer" um pattern | regex
pattern = r"[xu]u"

text = "uxxuxuu"

result = findall(pattern, text)

print(result)
