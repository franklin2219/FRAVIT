# Iterazione con l'utente per l'inserimento dei film nella piattaforma
class Utente:
    titolo = ""
    titolo_italiano = ""
    anno = 0
    genere = ""
    durata = 0
    voto = 0
    humor = 6
    ritmo = 6
    impegno = 6
    tensione = 6
    erotismo = 6
    peso_anno = 0
    peso_voto = 0
    peso_durata = 0
    genere_numerico = 0

    @classmethod
    def inseriscifilm(cls):
        cls.titolo = input(f"Inserisci il titolo originale del film/serieTV :")
        cls.titolo_italiano = input(f"Inserisci il titolo tradotto in italiano :")
        while cls.anno <= 1885 or cls.anno >= 2023:
            cls.anno = int(input("Inserisci l'anno di pubblicazione del film/serieTV :"))
        cls.genere = input(f"Inserisci il genere del film/serieTV :")
        while cls.durata > 240 or cls.durata < 1:
            cls.durata = int(input("Definisci la durata del film/serieTV :"))
        while cls.voto < 1 or cls.voto > 10:
            cls.voto = int(input("Inserisci il voto (un numero da 1 a 10) :"))
        while cls.humor < 0 or cls.humor > 5:
            cls.humor = int(input("Inserisci il valore il livello di Humor tra 0 a 5 : "))
        while cls.ritmo < 0 or cls.ritmo > 5:
            cls.ritmo = int(input("Inserisci il valore il livello di ritmo tra 0 a 5 : "))
        while cls.impegno < 0 or cls.impegno > 5:
            cls.impegno = int(input("Inserisci il valore il livello di impegno tra 0 a 5 : "))
        while cls.tensione < 0 or cls.tensione > 5:
            cls.tensione = int(input("Inserisci il valore il livello di tensione tra 0 a 5 : "))
        while cls.erotismo < 0 or cls.erotismo > 5:
            cls.erotismo = int(input("Inserisci il valore il livello di erotismo tra 0 a 5 : "))

        if cls.anno >= 2021:
            cls.peso_anno = 4
        elif cls.anno >= 2012:
            cls.peso_anno = 3
        elif cls.anno >= 2002:
            cls.peso_anno = 2
        else:
            cls.peso_anno = 1

        if cls.durata < 90:
            cls.peso_durata = 1
        elif cls.durata < 120:
            cls.peso_durata = 2
        elif cls.durata < 140:
            cls.peso_durata = 3
        else:
            cls.peso_durata = 4

        if cls.voto >= 8:
            cls.peso_voto = 4
        elif cls.voto >= 5:
            cls.peso_voto = 3
        elif cls.voto >= 3:
            cls.peso_voto = 2
        else:
            cls.peso_voto = 1

    @classmethod
    def richiestafilm(cls, self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+                  1)Animazione                                    +")
        print("+                  2)Drammatico                                    +")
        print("+                  3)Sentimentale                                  +")
        print("+                  4)Commedia                                      +")
        print("+                  5)Poliziesco                                    +")
        print("+                  6)Thriller                                      +")
        print("+                  7)Avventura                                     +")
        print("+                  8)Documentario                                  +")
        print("+                  9)Horror                                        +")
        print("+                  10)Azione                                       +")
        print("+                  11)Catastrofico                                 +")
        print("+                  12)Western                                      +")
        print("+                  13)Spionaggio                                   +")
        print("+                  14)Biografico                                   +")
        print("+                  15)Musicale                                     +")
        print("+                  16)Fantasy                                      +")
        print("+                  17)Guerra                                       +")
        print("+                  18)Grottesco                                    +")
        print("+                  19)Gangster                                     +")
        print("+                  20)Mitologico                                   +")
        print("+                  21)Storico                                      +")
        print("+                  22)Noir                                         +")
        print("+                  23)Supereroi                                    +")
        print("+                  24)Biblico                                      +")
        print("+                  25)Sportivo                                     +")
        print("+                  26)Sperimentale                                 +")
        print("+                  27)Cortometraggio                               +")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        while self.genere_numerico <= 0 or self.genere_numerico >= 28:
            self.genere_numerico = int(input("Inserisci il genere di Film/SerieTv che ti piacerebbe vedere :"))

        while self.humor < 0 or self.humor > 5:
            self.humor = int(input("Inserisci il valore il livello di Humor tra 0 a 5 :"))

        while self.ritmo < 0 or self.ritmo > 5:
            self.ritmo = int(input("Inserisci il valore il livello di ritmo tra 0 a 5 :"))

        while self.impegno < 0 or self.impegno > 5:
            self.impegno = int(input("Inserisci il valore il livello di impegno tra 0 a 5 :"))

        while self.tensione < 0 or self.tensione > 5:
            self.tensione = int(input("Inserisci il valore il livello di tensione tra 0 a 5 :"))

        while self.erotismo < 0 or self.erotismo > 5:
            self.erotismo = int(input("Inserisci il valore il livello di erotismo tra 0 a 5 :"))

        while self.peso_anno < 1 or self.peso_anno > 4:
            print("Inserisci il periodo cinematografico che preferisci:")
            print("1: piu' di 20 anni fa")
            print("2: dal 2002 al 2012")
            print("3: dal 2012 al 2021")
            print("4: dal 2021 in poi")
            self.peso_anno = int(input())


'''
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
'''