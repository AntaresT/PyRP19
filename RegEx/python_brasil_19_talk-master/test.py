import re


texto = """Watch the International Space Station pass
        overhead from several thousand worldwide locations.
        It is the third brightest object in the sky and easy
        to spot if you know when to look up.
        Visible to the naked eye, 485.748.999-78
        it looks like a fast-moving plane only much higher and
        traveling thousands of miles an hour faster!"""

texto2 = "1a2a3a"

texto3 = """
123 asd
0.3
ekfu 5.12312
"""

pattern = r"\d{3}\.\d{3}\.\d{3}-\d{2}"

padrao = r"([0-9]a)+"

paterno = r"^(\d+(\.\d+)?)"
# multiline pra poder pegar do começo da linha, nao do começo da string
result = [e[0] for e in re.findall(paterno, texto3, flags=re.MULTILINE)]

# print(findall(pattern, texto))
# print(findall(padrao, texto2))
print(result)
