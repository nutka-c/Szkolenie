slownik = {}
slownik["1"] = 'Tomek'
slownik["3"] = 'Kornelia'
slownik["14"] = 'Piotr'
slownik['16'] = [54,34, 5432, 442,2]
# print(slownik["1"])
print(slownik["16"][2])
slownik.pop('3')
slownik['14'] = 'Lukasz'
print(slownik)
print(slownik.keys())
print(slownik.values())
print(slownik.items())
print(slownik.get('imie'))
print(slownik.popitem())
