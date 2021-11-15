from Domain.cheltuiala import getNumar, creeazaCheltuiala, getTip, getSuma, getData


def adaugaCheltuiala(numar, suma, data, tip, lista):
    """
    adauga o cheltuiala intr-o lista
    :param numar: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: cheltuiala cu numarul dau sau None daca aceasta nu exista
    """
    cheltuiala = creeazaCheltuiala(numar, suma, data, tip)
    return lista + [cheltuiala]


def getByNumar(numar, lista):
    """
    da apartamentul cu numarul dat dintr-o lista
    :param numar: int
    :param lista: lista cu cheltuieli
    :return: un apartament
    """
    for cheltuiala in lista:
        if getNumar(cheltuiala) == numar:
            return cheltuiala
    return None


def stergeCheltuiala(numar, lista):
    """
    sterge cheltuiala cu numarul dat
    :param numar: int
    :param lista: lista cu cheltuieli
    :return: o lista de cheltuieli fara cheltuiala cu numarul dat
    """
    return [cheltuiala for cheltuiala in lista if getNumar(cheltuiala) != numar]


def modificaCheltuiala(numar, suma, data, tip, lista):
    '''
    :param numar: numarul apartamentului
    :param suma: suma cheltuielii
    :param data: data cheltuielii
    :param tip: tipul cheltuielii
    :param lista: lista de cheltuieli
    :return: lista modificata
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getData(cheltuiala) == data:
            cheltuialaNoua = creeazaCheltuiala(numar, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua

