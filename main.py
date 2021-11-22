#from Logic.CRUD import adaugaCheltuiala
#from Tests.testAll import runAllTest
from Logic.CRUD import adaugaCheltuiala
from Tests.testAll import runAllTest
from UI.commandLineConsole import menu
from UI.console import runMenu

def main():
    runAllTest()
    lista = []
    lista = adaugaCheltuiala(1, 250.0, "12.07.2010", "chirie", lista)
    lista = adaugaCheltuiala(2, 780.0, "22.05.2020", "apa", lista)
    #runMenu(lista)
    while True:
        x = input("Alegeti meniul:\n"
                  "Daca doriti meniul vechi tastati '1'\n"
                  "Daca doriti meniul nou tastati '2'\n")

        if x == '1':
            runMenu(lista)
        elif x == '2':
            menu(lista)


main()