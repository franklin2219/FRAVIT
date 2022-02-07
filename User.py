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
    genere_numerico = 0

    @classmethod
    def inserisciFilm(self):
        self.titolo=input(f"Inserisci il titolo originale del film/serieTV :")
        self.titolo_italiano=input(f"Inserisci il titolo tradotto in italiano :")
        while self.anno <= 1885 or self.anno >= 2023:
            self.anno=int(input("Inserisci l'anno di pubblicazione del film/serieTV :"))
        self.genere=input(f"Inserisci il genere del film/serieTV :")
        while self.durata >= 180 or self.durata <= 30:
            self.durata=int(input("Definisci la durata del film/serieTV :"))
        while self.voto <=1 or self.voto >= 10:
            self.voto=int(input("Inserisci il voto (un numero da 1 a 10) :"))
        while self.humor <=0 or self.humor >= 5:
            self.humor=int(input("Inserisci il valore il livello di Humor tra 0 a 5 : "))
        while self.ritmo <=0 or self.ritmo >= 5:
            self.ritmo=int(input("Inserisci il valore il livello di ritmo tra 0 a 5 : "))
        while self.impegno <=0 or self.impegno >= 5:
            self.impegno=int(input("Inserisci il valore il livello di impegno tra 0 a 5 : "))
        while self.tensione <=0 or self.tensione >= 5:
            self.tensione=int(input("Inserisci il valore il livello di tensione tra 0 a 5 : "))
        while self.erotismo <=0 or self.voto >= 5:
            self.erotismo=int(input("Inserisci il valore il livello di erotismo tra 0 a 5 : "))

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
            self.peso_durata = 2
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

        if self.genere=="Animazione":
            genere_numerico = 1
        elif self.genere=="Drammatico":
            genere_numerico = 2
        elif self.genere=="Sentimentale":
            genere_numerico = 3
        elif self.genere=="Commedia":
            genere_numerico = 4
        elif self.genere=="Poliziesco":
            genere_numerico = 5
        elif self.genere=="Thriller":
            genere_numerico = 6
        elif self.genere=="Avventura":
            genere_numerico = 7
        elif self.genere=="Documentario":
            genere_numerico = 8
        elif self.genere=="Horror":
            genere_numerico = 9
        elif self.genere=="Azione":
            genere_numerico = 10
        elif self.genere=="Catastrofico":
            genere_numerico = 11
        elif self.genere=="Western":
            genere_numerico = 12
        elif self.genere=="Spionaggio":
            genere_numerico = 13
        elif self.genere=="Biografico":
            genere_numerico = 14
        elif self.genere=="Musicale":
            genere_numerico = 15
        elif self.genere=="Fantasy":
            genere_numerico = 16
        elif self.genere=="Guerra":
            genere_numerico = 17
        elif self.genere=="Grottesco":
            genere_numerico = 18
        elif self.genere=="Gangster":
            genere_numerico = 19
        elif self.genere=="Mitologico":
            genere_numerico = 20
        elif self.genere=="Storico":
            genere_numerico = 21
        elif self.genere=="Noir":
            genere_numerico = 22
        elif self.genere=="Supereroi":
            genere_numerico = 23
        elif self.genere=="Biblico":
            genere_numerico = 24
        elif self.genere=="Sportivo":
            genere_numerico = 25
        elif self.genere=="Sperimentale":
            genere_numerico = 26
        elif self.genere=="Cortometraggio":
            genere_numerico = 27

    @classmethod
    def richiestaFilm(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+                1)Animazione                                  +")
        print("+                2)Drammatico                                  +")
        print("+                3)Sentimentale                                +")
        print("+                4)Commedia                                    +")
        print("+                5)Poliziesco                                  +")
        print("+                6)Thriller                                    +")
        print("+                7)Avventura                                   +")
        print("+                8)Documentario                                +")
        print("+                9)Horror                                      +")
        print("+                10)Azione                                     +")
        print("+                11)Catastrofico                               +")
        print("+                12)Western                                    +")
        print("+                13)Spionaggio                                 +")
        print("+                14)Biografico                                 +")
        print("+                15)Musicale                                   +")
        print("+                16)Fantasy                                    +")
        print("+                17)Guerra                                     +")
        print("+                18)Grottesco                                  +")
        print("+                19)Gangster                                   +")
        print("+                20)Mitologico                                 +")
        print("+                21)Storico                                    +")
        print("+                22)Noir                                       +")
        print("+                23)Supereroi                                  +")
        print("+                24)Biblico                                    +")
        print("+                25)Sportivo                                   +")
        print("+                26)Sperimentale                               +")
        print("+                27)Cortometraggio                             +")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        while self.genere_numerico <= 0 or self.genere_numerico >= 27:
            self.genere_numerico=int(input("Inserisci il genere di Film/SerieTv che ti piacerebbe vedere : "))
        while self.humor <= 0 or self.humor >=5:
            self.humor=int(input("Inserisci il valore il livello di Humor tra 0 a 5 : "))
        while  self.ritmo >= 6:
            self.ritmo=int(input("Inserisci il valore il livello di ritmo tra 0 a 5 : "))
        while self.impegno >= 6:
            self.impegno=int(input("Inserisci il valore il livello di impegno tra 0 a 5 : "))
        while self.tensione >= 6:
            self.tensione=int(input("Inserisci il valore il livello di tensione tra 0 a 5 : "))
        while self.voto >= 6:
            self.erotismo=int(input("Inserisci il valore il livello di erotismo tra 0 a 5 : "))
