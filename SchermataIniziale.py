from User import Utente
from ReteNeurale import PrevisionePrezzo
from SuggerimentoFilm import SuggerisciFilm

if __name__ == '__main__':
    utente1 = Utente()
    prezzo = PrevisionePrezzo()

    scelta = 0

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|                    GESTORE FILM E SERIE TV                       |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|                    1) Inserisci nuovo film                       |")
    print("|                    2) Suggerisci film                            |")
    print("|                                                                  |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    while scelta != '1' and scelta != '2':
        scelta = input("Inserisci il numero dell'operazione da effettuare : ")

    if scelta == '1':
        utente1.inseriscifilm()
        prezzo.prediciprezzo(utente1)
    if scelta == '2':
        utente1.richiestafilm()
        suggerimento = SuggerisciFilm(utente1)
pass
