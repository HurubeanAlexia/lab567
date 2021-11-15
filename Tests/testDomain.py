from Domain.cheltuiala import creeazaCheltuiala, getNumar, getSuma, getData, getTip


def testCheltuiala():
    cheltuiala = creeazaCheltuiala(1, 500.0, "12.03.2021", "intreținere")

    assert getNumar(cheltuiala) == 1
    assert getSuma(cheltuiala) == 500.0
    assert getData(cheltuiala) == "12.03.2021"
    assert getTip(cheltuiala) == "intreținere"
