def suma(x):
    liczba = str(x)
    wynik = 0
    for i in range(0, len(liczba)):
        wynik += int(liczba[i])
    return wynik

def potega(a, b):
    podstawa = 1
    for i in range(0, b):
        podstawa *= a
    return podstawa
maksimum = 0

for a in range(2, 100):
    for b in range(2, 100):
        t = suma(potega(a,b))
        if( t > maksimum):
            maksimum = t
print(maksimum)
