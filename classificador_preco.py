precos = [1.55, 1.42, 1.33, 1.80]
suporte = 1.40
resistencia = 1.70

for preco in precos:

    if preco < suporte:
        print(preco, "- Abaixo do suporte")

    elif preco > resistencia:
        print(preco, "- Rompimento de resistência")

    else:
        print(preco, "- Zona neutra")

