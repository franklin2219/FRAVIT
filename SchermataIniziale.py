from User import Utente
from ReteNeurale import PrevisionePrezzo

if __name__ == '__main__':
    utente1 = Utente
    prezzo = PrevisionePrezzo
    scelta=0

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|                    GESTORE FILM E SERIE TV                       |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|                    1) Inserisci nuovo film                       |")
    print("|                    2) Suggerisci film                            |")
    print("|                                                                  |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    while scelta != '1' and scelta != '2':
        scelta=input("Inserisci il numero dell'operazione da effettuare : ")

    if scelta == '1':
        utente1.titolo_Originale("")
        utente1.titolo_italiano("")
        utente1.anno_pubblicazione("")
        utente1.genere("")
        utente1.durata("")
        utente1.voto_critica("")
        utente1.voto_pubblico("")
        utente1.ritmo("")
        utente1.erotismo("")
        utente1.tensione("")
        utente1.impegno("")
        utente1.humor("")





pass

