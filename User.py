#Iterazione con l'utente per l'inserimento dei film nella piattaforma
class Utente:
    def __init__(self):
        Cioa="aws"
    def titolo_Originale(self):
        titolo=input(f"Inserisci il titolo originale del film/serieTV :")
        return titolo

    def titolo_italiano(self):
        titolo_italiano=input(f"Inserisci il titolo tradotto in italiano :")
        return titolo_italiano

    def anno_pubblicazione(self):
        anno=input(f"Inserisci l'anno di pubblicazione del film/serieTV :")
        return anno

    def genere(self):
        genere=input(f"Inserisci il genere del film/serieTV :")
        return genere

    def durata(self):
        durata=input(f"Definisci la durata del film/serieTV :")
        return durata

    def voto_critica(self):
        voto_critica=input("Inserisci il voto della critica (numerico) : ")
        return voto_critica

    def voto_pubblico(self):
        votoPubblico=input("Inserisci il voto del pubblico (numerico) : ")
        return votoPubblico

    def humor(self):
        humor=input("Inserisci il valore il livello di Humor tra 0 a 5 : ")
        return humor

    def ritmo(self):
        ritmo=input("Inserisci il valore il livello di ritmo tra 0 a 5 : ")
        return ritmo

    def impegno(self):
        impegno=input("Inserisci il valore il livello di impegno tra 0 a 5 : ")
        return impegno

    def tensione(self):
        tensione=input("Inserisci il valore il livello di tensione tra 0 a 5 : ")
        return tensione

    def erotismo(self):
        erotismo=input("Inserisci il valore il livello di erotismo tra 0 a 5 : ")
        return erotismo
