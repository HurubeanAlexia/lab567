from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from UI.console import showAll


def help():
    print("Daca doriti sa adaugati o cheltuiala tastati '1', dupa care "
          "separate prin virgula si fara spatii intre ele: "
          "numarul, suma, data, tipul")
    print("Daca doriti sa stergeti o cheltuiala tastati '2', dupa care "
          "dati nr-ul apartamentului al carui cheltuiala doriti sa "
          "fie stearsa.")
    print("Data doriti sa modificati o cheltuiala tastazi '3',dupa care "
          "separate prin virgula si fara spatii intre ele: "
          "numarul, suma, data, tipul")
    print("Daca doriti sa efectuati mai multe comenzi in acelasi timp "
          "dati valorile respective dupa modelul de mai sus, despartite "
          "prin ';'")

def menu(lista):
    ajutor = input("Daca aveti nevoie de ajutor tastati 'ajutor': ")
    if ajutor == 'ajutor':
        help()
    while True:
        comanda = input("Dati comenzile: ")
        commandAll = comanda.split(';')
        stop = 0
        for i in range (len(commandAll)):
            command = commandAll[i]
            command = command.split(',')
            if command[0] == '1':
                numar = command[1]
                suma = command[2]
                data = command[3]
                tip = command[4]
                lista = adaugaCheltuiala(numar, suma, data, tip, lista)
            elif command[0] == '2':
                numar = command[1]
                lista = stergeCheltuiala(numar, lista)
            elif command[0] == '3':
                numar = command[1]
                suma = command[2]
                data = command[3]
                tip = command[4]
                lista = modificaCheltuiala(numar, suma, data, tip, lista)
            elif command[0] == 'a':
                showAll(lista)
            elif command[0] == 'x':
                stop = 1
        if stop == 1:
            break


