def produs(*args):
    rezultat = 1
    for numar in args:
        rezultat *= numar
    return rezultat

# Exemplu de utilizare:
print(produs(2, 3, 4))  # Va afișa 24 (2 * 3 * 4)


def afiseaza_lista(lista):
    for numar in lista:
        print(numar)

# Exemplu de utilizare:
numere = [1, 2, 3, 4, 5]
afiseaza_lista(numere)



def afiseaza_lista_dictionare(lista_dictionare):
    for dictionar in lista_dictionare:
        for cheie, valoare in dictionar.items():
            print(f"{cheie}: {valoare}")

# Exemplu de utilizare:
lista_dictionare = [
    {"nume": "Ana", "varsta": 25},
    {"nume": "Ion", "varsta": 30},
    {"nume": "Maria", "varsta": 22}
]
afiseaza_lista_dictionare(lista_dictionare)
