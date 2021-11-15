def creeazaCheltuiala(numar, suma, data, tip):
    """
    creeaza un dictionar care reprezinta un apartament
    :param numar: int
    :param suma: float
    :param data: string
    :param tip: string
    :return: un dictionar ce contine un apartament
    """
    return {
        "numar": numar,
        "suma": suma,
        "data": data,
        "tip": tip,
    }

def getNumar(cheltuiala):
    '''
    da numarul apartamentului
    :param cheltuiala: dictionarul care contine un apartament
    :return: numarul apartamentului
    '''
    return cheltuiala["numar"]

def getSuma(cheltuiala):
    return cheltuiala["suma"]

def getData(cheltuiala):
    return cheltuiala["data"]

def getTip(cheltuiala):
    return cheltuiala["tip"]

def toString(cheltuiala):
    return "Numar: {}, Suma: {}, Data: {}, Tip: {}".format(
        getNumar(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala)
    )

