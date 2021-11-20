#from Logic.CRUD import adaugaCheltuiala
#from Tests.testAll import runAllTest
from Logic.CRUD import adaugaCheltuiala
from Tests.testAll import runAllTest
from UI.console import runMenu

def main():
    runAllTest()
    lista = []
    lista = adaugaCheltuiala(1, 250.0, "12.07.2010", "chirie", lista)
    lista = adaugaCheltuiala(2, 780.0, "22.05.2020", "apa", lista)
    #runMenu(lista)
    while True:
        optiune = input("Dati optiunea:")
        if optiune == "1":
            runMenu(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")
main()