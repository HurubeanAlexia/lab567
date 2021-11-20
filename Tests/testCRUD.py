from Domain.cheltuiala import getNumar, getSuma, getData, getTip
from Logic.CRUD import adaugaCheltuiala, getByNumar, modificaCheltuiala, stergeCheltuiala


def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, 500.0, "12.03.2021", "intreținere", lista)

    assert len(lista) == 1
    assert getNumar(getByNumar(1, lista)) == 1
    assert getSuma(getByNumar(1, lista)) == 500.0
    assert getData(getByNumar(1, lista)) == "12.03.2021"
    assert getTip(getByNumar(1, lista)) == "intreținere"

def testModificaCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, 300.0, "15.10.2021", "intretinere", lista)
    lista = modificaCheltuiala(1, 250.0, "15.10.2021", "gaz", lista)
    assert len(lista) == 1
    assert getNumar(lista[0]) == 1
    assert getSuma(lista[0]) == 250.0
    assert getData(lista[0]) == "15.10.2021"
    assert getTip(lista[0]) == "gaz"

def testStergeCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, 560.0, "12.03.2020", "intreținere", lista)
    lista = adaugaCheltuiala(2, 780.0, "18.04.2018", "apa", lista)
    lista = stergeCheltuiala(1, lista)
    #assert len(lista) == 1
    assert lista == [(2, 780.0, "18.04.2018", "apa")]