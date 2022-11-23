liczby = 45, 76, 76.5, 34, 2, 0, 33, 444, 33
print(type(liczby))
print(liczby)
print(liczby[2])
print(liczby.count(0))

imiona = "Tomek", "Lukasz", "Piotr", "Kornelia"
i1, i2, i3, i4 = imiona
print(i1)
print(i2)
print(i3)
print(i4)
i1, i2, *i3 = imiona
print(i1)
print(i2)
print(i3[1])
print(i3[0:2])

krotka = ()
lista = []
lista.append(i2)
lista.append(i3)
lista.append("Tomek")
lista.insert(1, 2021)
print(lista)
lista.sort()
lista.reverse()
lista.remove("Maciej")

nowa_lista = lista
nowa_lista2 = lista.copy()
nowa_lista.pop()
nowa_lista2.append("TEST")
print ("stara lista", lista)
print("id starej listy" id(lista))
print("nowa lista", nowa_lista)
print("ID nowej listy", id(nowa_lista))
print("nowa 2 lista", nowa_lista2)
print(nowa_lista+nowa_lista2)
nowa_lista.extend(nowa_lista2)
print(nowa_lista)