from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
# from Logic.functionalitati import reducereSuma
from Logic.functionalitati import crestereSuma, sumaMaximaTip, ordonareCheltuieli, verificareData, sumaLunara, \
    stergereaTuturorCheltuielilor


def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("4. Maximul cheltuielilor pentru fiecare tip")
    print("5. Cresterea valorii dintr-o anumita data")
    print("6. Ordonarea descrescatoare a cheltuielilor")
    print("7. Afisarea sumelor lunare pentru fiecare apartament")
    print("8. Stergerea tuturor cheltuielilor pentru un apartament")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare cheltuiala")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista, undoList, redoList):
    try:
        numar = int(input("Dati numarul: "))
        suma = float(input("Dati suma: "))
        data = input("Dati data: ")
        tip = input('Dati tipul: ')
        rezultat = adaugaCheltuiala(numar, suma, data, tip, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeCheltuiala(lista, undoList, redoList):
    try:
        numar = int(input("Dati numarul cheltuielii de sters: "))
        rezultat = stergeCheltuiala(numar, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaCheltuiala(lista, undoList, redoList):
    try:
        numar = int(input("Dati numarul cheltuielii de modificat: "))
        suma = float(input("Dati noua suma: "))
        data = input("Dati noua data: ")
        tip = input('Dati noul tip: ')
        rezultat = modificaCheltuiala(numar, suma, data, tip, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiSumaMaximaTip(lista):
    try:
        rezultat = sumaMaximaTip(lista)
        if rezultat[0] != 0:
            print("Maximul cheltuielilor pentru chirie este de " + str(rezultat[0]) + " lei")
        else:
            print("Nu exista cheltuiala de tip chirie")
        if rezultat[1] != 0:
            print("Maximul cheltuielilor pentru intretinere este de " + str(rezultat[1]) + " lei")
        else:
            print("Nu exista cheltuiala de tip intretinere")
        if rezultat[2] != 0:
            print("Maximul cheltuielilor pentru apa este de " + str(rezultat[2]) + " lei")
        else:
            print("Nu exista cheltuiala de tip apa")
        if rezultat[3] != 0:
            print("Maximul cheltuielilor pentru gaz este de " + str(rezultat[3]) + " lei")
        else:
            print("Nu exista cheltuiala de tip gaz")
        if rezultat[4] != 0:
            print("Maximul cheltuielilor pentru curent este de " + str(rezultat[4]) + " lei")
        else:
            print("Nu exista cheltuiala de tip curent")
        return sumaMaximaTip(lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiCrestereSuma(lista):
    try:
        tip = input("Dati data in care creste suma: ")
        valoare = input("Dati valoarea cu care creste suma: ")
        return crestereSuma(tip, valoare, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiOrdonareCheltuieli(lista):
    return ordonareCheltuieli(lista)


def uiStergereaTuturorCheltuielilor(lista):
    numar = int(input("Dati numarul apartamentului al carui cheltuieli vor fi sterse: "))
    return stergereaTuturorCheltuielilor(numar, lista)


def uiVerificareData(lista):
    data_tastatura = input("dati data de la tastatura, in format DD.MM.YYYY cu tot cu '.' . ")
    number = float(input("dati un numar, pe care doriti sa il adaugat la suma din data ceruta"))
    rezultat = verificareData(data_tastatura, lista, number)
    return rezultat


def uiSumaLunara(lista):
    dictionary = sumaLunara(lista)
    for numar in dictionary:
        for year in dictionary[numar]:
            for month in dictionary[numar][year]:
                print("Apartamentul {} are cheltuieli in valoare de {} in anul {} si respectiv luna {} ".format(
                    numar,
                    dictionary[numar][year][month],
                    year,
                    month
                ))


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiSumaMaximaTip(lista)
        elif optiune == "5":
            lista = uiCrestereSuma(lista)
        elif optiune == "6":
            lista = uiOrdonareCheltuieli(lista)
        elif optiune == "7":
            lista = uiSumaLunara(lista)
        elif optiune == "8":
            lista = uiStergereaTuturorCheltuielilor(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
