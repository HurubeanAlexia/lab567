from Domain.cheltuiala import getTip, getSuma, creeazaCheltuiala, getNumar, getData


def crestereSuma(data, valoare, lista):
    '''
    adauga la suma o valoare data de utilizator apartamentelor dintr-o anumita data
    :param data: data pentru care va fi modificata suma
    :param valoare: numarul cu care va creste suma
    :param lista: lista de cheltuieli
    :return:
    '''
    nouaLista = []
    for cheltuiala in lista:
        if getData(cheltuiala) == data:
            nouaSuma = getSuma(cheltuiala) + valoare
            cheltuialaNoua = creeazaCheltuiala(getNumar(cheltuiala), nouaSuma, getData(cheltuiala), getTip(cheltuiala))
            nouaLista.append(cheltuialaNoua)
        else:
            nouaLista.append(cheltuiala)
    return nouaLista

