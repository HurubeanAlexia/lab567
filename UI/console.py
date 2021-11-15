from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
#from Logic.functionalitati import reducereSuma
from Logic.functionalitati import crestereSuma


def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("4. Adaugarea valorii dupa data")
    print("a. Afisare cheltuiala")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista):
    numar = int(input("Dati numarul: "))
    suma = float(input("Dati suma: "))
    data = input("Dati data: ")
    tip = input('Dati tipul: ')
    return adaugaCheltuiala(numar, suma, data, tip, lista)


def uiStergeCheltuiala(lista):
    numar = int(input("Dati numarul cheltuielii de sters: "))
    return stergeCheltuiala(numar, lista)


def uiModificaCheltuiala(lista):
    numar = int(input("Dati numarul cheltuielii de modificat: "))
    suma = float(input("Dati noua suma: "))
    data = input("Dati noua data: ")
    tip = input('Dati noul tip: ')
    return modificaCheltuiala(numar, suma, data, tip, lista)


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiCrestereSuma(lista):
    tip = input("Dati data in care creste suma: ")
    valoare = int(input("Dati valoarea cu care creste suma: "))
    return crestereSuma(tip, valoare, lista)


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista)
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista)
        elif optiune == "4":
            lista = uiCrestereSuma(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
