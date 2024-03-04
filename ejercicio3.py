lista_primera = ["daniela","ana","roberto","carlos","cristiano"]
lista_2 = []
for elemento in lista_primera:
    if len(elemento) > 5:
        lista_2.append(elemento)
print(lista_2)