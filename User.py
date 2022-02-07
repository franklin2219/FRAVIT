#Iterazione con l'utente per l'inserimento dei film nella piattaforma
class Utente:
    def __init__(self):
        titolo = ""
        titolo_italiano = ""
        anno = 0
        genere = ""
        durata = 0
        voto = 0
        humor = 0
        ritmo = 0
        impegno = 0
        tensione = 0
        erotismo = 0
        peso_anno = 0
        peso_voto = 0
        peso_durata = 0
    @classmethod
    def inserisciFilm(self):
        titolo=input(f"Inserisci il titolo originale del film/serieTV :")
        titolo_italiano=input(f"Inserisci il titolo tradotto in italiano :")
        anno=input(f"Inserisci l'anno di pubblicazione del film/serieTV :")
        genere=input(f"Inserisci il genere del film/serieTV :")
        durata=input(f"Definisci la durata del film/serieTV :")
        voto=input("Inserisci il voto (numerico) :")
        humor=input("Inserisci il valore il livello di Humor tra 0 a 5 : ")
        ritmo=input("Inserisci il valore il livello di ritmo tra 0 a 5 : ")
        impegno=input("Inserisci il valore il livello di impegno tra 0 a 5 : ")
        tensione=input("Inserisci il valore il livello di tensione tra 0 a 5 : ")
        erotismo=input("Inserisci il valore il livello di erotismo tra 0 a 5 : ")

        if anno >= "2021":
            peso_anno = 4
        elif anno >= 2012:
            peso_anno = 3
        elif anno >= 2002:
            peso_anno = 2
        else: peso_anno = 1

        if durata < "90":
            peso_durata = 4
        elif durata < "120":
            peso_durata = 3
        elif durata < "140":
            peso_durata = 2
        else: peso_durata = 1

        if voto >= "8":
            peso_voto = 4
        elif voto >= 5:
            peso_voto = 3
        elif voto >= 3:
            peso_voto = 2
        else: peso_voto = 1