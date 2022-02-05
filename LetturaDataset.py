import pandas as pd

film= pd.read_csv("/Users/srancescosasso/SimulatoreNoleggioAcquisto/filmtv_movies - ITA.csv")

#print(film.head())
#print(film.columns)

#Y=film['titolo_originale']
#print(Y.head(10))

#gianni=Y.loc[3]#posso associare ad una stringa l'elemento presente in quella posizione
#print(gianni)

valore =input("Inserisci il nome di un film ")
esito=0
for titolo in film['titolo_originale']:
    if titolo == valore:
        print(valore)
        esito=1
if not esito:
    print("Scrivi bene")

