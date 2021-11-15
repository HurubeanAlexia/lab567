from Domain.cheltuiala import getSuma
from Logic.CRUD import adaugaCheltuiala
from Logic.functionalitati import crestereSuma


def testFunctionalitati():
    lista = []
    lista = adaugaCheltuiala(1, 300, "15.10.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 350, "15.10.2021", "canal", lista)
    lista = adaugaCheltuiala(3, 1050, "17.10.2021", "alte cheltuieli", lista)
    lista = crestereSuma("15.10.2021", 120, lista)
    assert getSuma(lista[0]) == 420
    assert getSuma(lista[1]) == 470

