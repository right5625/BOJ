cena = list(input().split())
print(
    cena[0]
    + ("'" + cena[1][1] if cena[0][-1] == cena[1][0] else cena[1])
    + ("'" + cena[2][1] if cena[1][-1] == cena[2][0] else cena[2])
)
