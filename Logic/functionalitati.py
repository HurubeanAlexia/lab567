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
            nouaSuma = getSuma(cheltuiala) + float(valoare)
            cheltuialaNoua = creeazaCheltuiala(getNumar(cheltuiala), nouaSuma, getData(cheltuiala), getTip(cheltuiala))
            nouaLista.append(cheltuialaNoua)
        else:
            nouaLista.append(cheltuiala)
    return nouaLista

def sumaMaximaTip(lista):
    '''
    determina cea mai mare valoare in functie de tip
    :param lista: list
    :return: o lista ce contine maximul pentru fiecare tip de cheltuiala
    '''
    rezultat = []
    maximChirie = 0
    maximIntretinere = 0
    maximApa = 0
    maximGaz = 0
    maximCurent = 0

    for cheltuiala in lista:
        if getTip(cheltuiala) == "chirie" and getSuma(cheltuiala) > maximChirie:
             maximChirie = getSuma(cheltuiala)
        elif getTip(cheltuiala) == "intretinere" and getSuma(cheltuiala) > maximIntretinere:
             maximIntretinere = getSuma(cheltuiala)
        elif getTip(cheltuiala) == "apa" and getSuma(cheltuiala) > maximApa:
             maximApa = getSuma(cheltuiala)
        elif getTip(cheltuiala) == "gaz" and getSuma(cheltuiala) > maximGaz:
             maximGaz = getSuma(cheltuiala)
        elif getTip(cheltuiala) == "curent" and getSuma(cheltuiala) > maximCurent:
             maximCurent = getSuma(cheltuiala)
    rezultat = [maximChirie, maximIntretinere, maximApa, maximGaz, maximCurent]
    return rezultat

def stergereaTuturorCheltuielilor(numar, lista):
    """
    sterge toate cheltuielile pentru un apartamnent
    :param numar: numarul apartamentului
    :param lista: lista de cheltuieli
    :return: lista de cheltuili dupa stergere
    """

    nouaLista = []
    for cheltuiala in lista:
        if getNumar(cheltuiala) != numar:
            nouaLista.append(cheltuiala)
    return nouaLista

def ordonareCheltuieli(lista):
    '''
    ordoneaza descrescator in functie de suma
    :param lista: lista de cheltuieli
    :return: lista ordonata
    '''
    n = len(lista)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if getSuma(lista[j]) < getSuma(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                already_sorted = False
        if already_sorted:
            break
    return lista

def corectitudineData(data_tastatura):
    """
    vedrifica corectitudinea datii
    :param data_tastatura: o data de la tastatura
    :return: True, daca data este scrisa corect si False in caz contrar
    """
    list_of_string = list(data_tastatura)
    if len(list_of_string) < 10 or len(list_of_string) > 10:
        return False
    if list_of_string[2] != list_of_string[5] and list_of_string[5] != '.':
        return False
    count = 0
    for x in list_of_string:
        if x == '.':
            count = count + 1
    if count != 2:
        return False
    if list_of_string[0] == '0':
        day = int(list_of_string[1])
    else:
        new_string = list_of_string[0] + list_of_string[1]
        day = int(new_string)
    if list_of_string[3] == '0':
        month = int(list_of_string[4])
    else:
        new_string = list_of_string[3] + list_of_string[4]
        month = int(new_string)
    if month > 12:
        return False
    if month == 1 and day > 31:
        return False
    if month == 2 and day > 29:
        return False
    if month == 3 and day > 31:
        return False
    if month == 4 and day > 30:
        return False
    if month == 5 and day > 31:
        return False
    if month == 6 and day > 30:
        return False
    if month == 7 and day > 31:
        return False
    if month == 8 and day > 31:
        return False
    if month == 9 and day > 30:
        return False
    if month == 10 and day > 31:
        return False
    if month == 11 and day > 30:
        return False
    if month == 12 and day > 31:
        return False
    return True

def verificareData(data_tastatura, lista, number):
    '''

    :param data_tastatura: o data de la tastatura
    :param lista:
    :param numar:
    :return:
    '''
    if corectitudineData(data_tastatura) is False:
        return []
    nouaLista = []
    for cheltuiala in lista:
        if getData(cheltuiala) == data_tastatura:
            suma = getSuma(cheltuiala) + number
            numar = getNumar(cheltuiala)
            tip = getTip(cheltuiala)
            data = getData(cheltuiala)
            cheltuialaNoua = creeazaCheltuiala(numar, suma, data, tip)
            nouaLista.append(cheltuialaNoua)
        else:
            nouaLista.append(cheltuiala)
    return nouaLista

def sumaLunara(lista):
    """
    :param lista:
    :return:
    """
    dictionary = {}
    for cheltuiala in lista:
        numar = getNumar(cheltuiala)
        suma = getSuma(cheltuiala)
        data = getData(cheltuiala)
        list_of_string = list(data)
        if list_of_string[3] == '0':
            month = int(list_of_string[4])
        else:
            new_string = list_of_string[3] + list_of_string[4]
            month = int(new_string)
        year = list_of_string[6] + list_of_string[7] + list_of_string[8] + list_of_string[9]
        year_1 = int(year)
        if numar in dictionary:
            if year in dictionary[numar]:
                if month in dictionary[numar][year]:
                    dictionary[numar][year][month] = dictionary[numar][year][month] + suma
                else:
                    dictionary[numar][year][month] = suma
            else:
                dictionary[numar][year] = {month : suma}
        else:
            dictionary[numar] = {year: {month: suma}}
    return dictionary