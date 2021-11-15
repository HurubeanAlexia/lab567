from Domain.cheltuiala import getNumar, getSuma, getData, getTip
from Logic.CRUD import adaugaCheltuiala, getByNumar


def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, 500.0, "12.03.2021", "intreținere", lista)

    assert len(lista) == 1
    assert getNumar(getByNumar(1, lista)) == 1
    assert getSuma(getByNumar(1, lista)) == 500.0
    assert getData(getByNumar(1, lista)) == "12.03.2021"
    assert getTip(getByNumar(1, lista)) == "intreținere"
