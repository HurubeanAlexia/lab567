from Domain import cheltuiala
from Domain.cheltuiala import getSuma, getNumar, getData, getTip, creeazaCheltuiala
from Logic.CRUD import adaugaCheltuiala
from Logic.functionalitati import crestereSuma, sumaMaximaTip, ordonareCheltuieli, verificareData, corectitudineData, \
    sumaLunara


def testCrestereSuma():
    lista = []
    lista = adaugaCheltuiala(1, 300.0, "15.10.2021", "intretinere", lista)
    lista = adaugaCheltuiala(2, 350.0, "15.10.2021", "canal", lista)
    lista = adaugaCheltuiala(3, 1050.0, "17.10.2021", "alte cheltuieli", lista)
    lista = crestereSuma("15.10.2021", 120.0, lista)
    assert getSuma(lista[0]) == 420
    assert getSuma(lista[1]) == 470


def testSumaMaximaTip():
    lista = []
    lista = adaugaCheltuiala(1, 900.0, "15.10.2021", "chirie", lista)
    lista = adaugaCheltuiala(2, 450.0, "15.10.2021", "apa", lista)
    lista = adaugaCheltuiala(3, 1050.0, "17.10.2021", "gaz", lista)
    lista = adaugaCheltuiala(4, 516.0, "10.10.2021", "apa", lista)
    rezultat = sumaMaximaTip(lista)
    assert rezultat[0] == 900.0
    assert rezultat[2] == 516.0

def testOrdonareCheltuieli():
    lista = []
    lista = adaugaCheltuiala(25, 200, "03.05.2021", "apa", lista)
    lista = adaugaCheltuiala(25, 200.5, "03.05.2021", "apa", lista)
    lista = adaugaCheltuiala(24, 140, "03.05.2021", "apa", lista)
    lista = ordonareCheltuieli(lista)
    assert lista == [[25, 200.5, "03.05.2021", 'apa'], [25, 200, "03.05.2021", 'apa'], [24, 140, "03.05.2021", 'apa']]


def testVerificareData():
    lst = []
    lst = adaugaCheltuiala(25, 200, "03.05.2021", " ", lst)
    lst = adaugaCheltuiala(25, 200, "03.05.2021", " ", lst)
    lst = adaugaCheltuiala(24, 200, "03.05.2021", " ", lst)
    lst = adaugaCheltuiala(24, 200, "04.05, 2021", " ", lst)
    data_tastatura = "02.03.2021"
    lst = verificareData(data_tastatura, lst, 5)
    assert lst == [[25, 200, '03.05.2021', ' '], [25, 200, '03.05.2021', ' '], [24, 200, '03.05.2021', ' '],
                   [24, 200, '04.05, 2021', ' ']]



def testCorectitudineData():
    assert corectitudineData("22.30.2002") is False
    assert corectitudineData("31.04.2002") is False
    assert corectitudineData("30.03.2002") is True

def testSumaLunara():
    lst = []
    lst = adaugaCheltuiala(25, 200, "03.05.2021", "apa", lst)
    lst = adaugaCheltuiala(25, 200.5, "03.05.2021", "apa", lst)
    lst = adaugaCheltuiala(24, 140, "03.05.2020", "gaz", lst)
    lst = adaugaCheltuiala(25, 150, "05.05.2020", "intretinere", lst)
    lst = adaugaCheltuiala(25, 150, "09.10.2021", "intretinere", lst)
    assert sumaLunara(lst) == {25: {'2021': {5: 400.5, 10: 150}, '2020': {5: 150}}, 24: {'2020': {5: 140}}}