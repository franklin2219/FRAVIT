from User import Utente
import sys
from PrevisionePrezzo import PrevisionePrezzo
from SuggerimentoFilm import SuggerisciFilm
from SceltaSezioni import ScegliSezioni

if __name__ == '__main__':
    utente1 = Utente()
    prezzo = PrevisionePrezzo()
    predicisezione = ScegliSezioni()
    scelta = 0

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|                    GESTORE FILM E SERIE TV                       |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|                    1) Inserisci nuovo film                       |")
    print("|                    2) Suggerisci film                            |")
    print("|                    3) Menu film                                  |")
    print("|                    4) Inserisci film in una sezione              |")
    print("|                    5) Esci                                       |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    while scelta != '1' and scelta != '2' and scelta != '3' and scelta != '4' and scelta != '5':
        scelta = input("Inserisci il numero dell'operazione da effettuare : ")

    if scelta == '1':
        utente1.inseriscifilm()
        prezzo.prediciprezzo(utente1)
    if scelta == '2':
        utente1.richiestafilm()
        suggerimento = SuggerisciFilm(utente1)
    if scelta == '4':
        utente1.inserisciinsezione()
        predicisezione.inseriscivalori(utente1)
    if scelta == '5':
        print("A PRESTO!")
        sys.exit()

pass
