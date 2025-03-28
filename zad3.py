"""
policz ilosc wystepowan kazdego elementu w zdaniu. wypisz najczesciej wystepujaca litere.
Spacje sie nie licza
"""

data = "W PYTHONIE SLOWNIKI ZASTEPUJA HASHMAPY"
data = data.replace(" ", "")
dict={}
for elem in data:
    if dict.get(elem):
        dict[elem] += 1
    else:
        dict[elem] = 1

print(dict)
max_key = max(dict, key=dict.get)

print("Key with max value:", max_key)