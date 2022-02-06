from User import Utente

if __name__ == '__main__':
    utente1 = Utente
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|                    GESTORE FILM E SERIE TV                       |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|                    1) Inserisci nuovo film                       |")
    print("|                    2) Suggerisci film                            |")
    print("|                                                                  |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    scelta=input("Inserisci il numero dell'operazione da effettuare : ")

    if scelta == "1":
        utente1.titolo_Originale()


pass

