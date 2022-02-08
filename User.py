class Utente:
    titolo = ""
    titolo_italiano = ""
    anno = 0
    genere = ""
    durata = 0
    voto = 0
    humor = -1
    ritmo = -1
    impegno = -1
    tensione = -1
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
        cls.inserisciinsezione()

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
    def richiestafilm(cls):
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
        while cls.genere_numerico <= 0 or cls.genere_numerico >= 28:
            cls.genere_numerico = int(input("Inserisci il genere di Film/SerieTv che ti piacerebbe vedere :"))

        cls.inserisciinsezione()

        while cls.peso_anno < 1 or cls.peso_anno > 4:
            print("Inserisci il periodo cinematografico che preferisci:")
            print("1: piu' di 20 anni fa")
            print("2: dal 2002 al 2012")
            print("3: dal 2012 al 2021")
            print("4: dal 2021 in poi: ")
            cls.peso_anno = int(input("--> "))

    @classmethod
    def inserisciinsezione(cls):
        while cls.humor < 0 or cls.humor > 5:
            cls.humor = int(input("Inserisci il valore il livello di humor tra 0 a 5 :"))
        while cls.ritmo < 0 or cls.ritmo > 5:
            cls.ritmo = int(input("Inserisci il valore il livello di ritmo tra 0 a 5 :"))
        while cls.impegno < 0 or cls.impegno > 5:
            cls.impegno = int(input("Inserisci il valore il livello di impegno tra 0 a 5 :"))
        while cls.tensione < 0 or cls.tensione > 5:
            cls.tensione = int(input("Inserisci il valore il livello di tensione tra 0 a 5 :"))
