#Iterazione con l'utente per l'inserimento dei film nella piattaforma
class Utente:
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
        self.titolo=input(f"Inserisci il titolo originale del film/serieTV :")
        self.titolo_italiano=input(f"Inserisci il titolo tradotto in italiano :")
        self.anno=int(input("Inserisci l'anno di pubblicazione del film/serieTV :"))
        self.genere=input(f"Inserisci il genere del film/serieTV :")
        self.durata=int(input("Definisci la durata del film/serieTV :"))
        self.voto=int(input("Inserisci il voto (numerico) :"))
        self.humor=input("Inserisci il valore il livello di Humor tra 0 a 5 : ")
        self.ritmo=input("Inserisci il valore il livello di ritmo tra 0 a 5 : ")
        self.impegno=input("Inserisci il valore il livello di impegno tra 0 a 5 : ")
        self.tensione=input("Inserisci il valore il livello di tensione tra 0 a 5 : ")
        self.erotismo=input("Inserisci il valore il livello di erotismo tra 0 a 5 : ")

        if self.anno >= 2021:
            self.peso_anno = 4
        elif self.anno >= 2012:
            self.peso_anno = 3
        elif self.anno >= 2002:
            self.peso_anno = 2
        else: self.peso_anno = 1

        if self.durata < 90:
            self.peso_durata = 1
        elif self.durata < 120:
            peso_durata = 2
        elif self.durata < 140:
            self.peso_durata = 3
        else: self.peso_durata = 4

        if self.voto >= 8:
            self.peso_voto = 4
        elif self.voto >= 5:
            self.peso_voto = 3
        elif self.voto >= 3:
            self.peso_voto = 2
        else: self.peso_voto = 1