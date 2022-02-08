import pandas as pd

class MenuGestioneFilm:

    scelta=0

    menu = pd.read_csv("dataset_completo.csv", delimiter=";")

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|                        CONTROLLO MAGAZZINO                       |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|                    1) Controllo film a disposizione              |")
    print("|                    2) Film più votati                            |")
    print("|                    3) Totale film a disposizione                 |")
    print("|                    4) Torna indietro                             |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    while scelta != '1' and scelta != '2' and scelta != '3' and scelta != '4':
        scelta = input("Inserisci il numero dell'operazione da effettuare : ")
    if scelta == '1':
        print(menu)


