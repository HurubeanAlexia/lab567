from Logic.CRUD import adaugaCheltuiala
from Tests.testAll import runAllTest
from UI.console import runMenu

if __name__ == '__main__':
    #print_hi('PyCharm')
    runAllTest()
    lista = []
    lista = adaugaCheltuiala(1, 250.0, "12.07.2010", "chirie", lista)
    lista = adaugaCheltuiala(2, 780.0, "22.05.2020", "chirie", lista)
    runMenu(lista)
