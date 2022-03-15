from Film import Film
import sys
from PrevisionePrezzo import PrevisionePrezzo
from SuggerimentoFilm import SuggerisciFilm
from SceltaSezioni import ScegliSezioni
from prolog import ControllaConvenienza

if __name__ == '__main__':
    film = Film()
    prezzo = PrevisionePrezzo()
    predicisezione = ScegliSezioni()
    controllaConvenienza = ControllaConvenienza()
    scelta = -1
    while scelta != 5:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("|                    GESTORE FILM E SERIE TV                       |")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("|                    1) Predici Prezzo                             |")
        print("|                    2) Suggerisci film                            |")
        print("|                    3) Trova Sezione Negozio                      |")
        print("|                    4) Precision,Recall,Mae,Accuratezza           |")
        print("|                    5) Controlla se conviene prendere un film     |")
        print("|                    6) Esci                                       |")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        while scelta != '1' and scelta != '2' and scelta != '3' and scelta != '4' and scelta != '5' and scelta != '6':
            scelta = input("Inserisci il numero dell'operazione da effettuare :")

        if scelta == '1':
            film.inseriscifilm()
            prezzo.prediciprezzo(film)
        if scelta == '2':
            film.richiestafilm()
            suggerimento = SuggerisciFilm(film)
        if scelta == '3':
            film.inserisciinsezione()
            predicisezione.inseriscivalori(film)
        if scelta == '4':
            prezzo.datiPredizioni(prezzo.precisione, prezzo.richiamo, prezzo.maeTRAIN, prezzo.maeTEST,
                                  prezzo.accuratezza)
        if scelta == '5':
            controllaConvenienza.convenienza(input("Inserisci il voto del film : "),input("Inserisci il prezzo del film : "))
        if scelta == '6':
            print("A PRESTO!")
            sys.exit()
        scelta = -1
        film.resettavalori()
pass
