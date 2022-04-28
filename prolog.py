import pytholog as pl


class ControllaConvenienza:
    def convenienza(cls):

        kb = pl.KnowledgeBase("film")
        kb.from_file("myKb.pl")
        scelta = -1
        while scelta != '9':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("|     1) Trova genere film                                           |")
            print("|     2) Trova durata film                                           |")
            print("|     3) Mostra film in proiezione in una sala                       |")
            print("|     4) Mostra addetto alla proiezione di una sala                  |")
            print("|     5) Trova film di un determinato genere                         |")
            print("|     6) Trova film di una determinata durata                        |")
            print("|     7) Mostra in quale sala è proiettato un film                   |")
            print("|     8) Mostra in quale sala è assegnato un addetto alla proiezione |")
            print("|     9) Torna indietro                                              |")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            scelta = input("Inserisci il numero dell'operazione da effettuare :")

            if scelta == '1':
                nomefilm = str(input("inserisci il nome del film: ")).lower()
                print(kb.query(pl.Expr("film("+nomefilm+",T)"))[0])
            if scelta == '2':
                nomefilm = str(input("inserisci il nome del film: ")).lower()
                print(kb.query(pl.Expr("durata("+nomefilm+",D)"))[0])
            if scelta == '3':
                nomesala = str(input("inserisci il nome della sala: ")).lower()
                listaproiezioni = list(kb.query(pl.Expr("sala(T,"+nomesala+")")))
                for film in listaproiezioni:
                    print(film)
            if scelta == '4':
                nomesala = str(input("inserisci il nome della sala: ")).lower()
                print(kb.query(pl.Expr("addetto("+nomesala+",A)"))[0])
            if scelta == '5':
                genere = str(input("inserisci il genere: ")).lower()
                listafilm = list(kb.query(pl.Expr("film(F,"+genere+")")))
                for film in listafilm:
                    print(film)
            if scelta == '6':
                durata = str(input("inserisci la durata: ")).lower()
                listafilm = list(kb.query(pl.Expr("durata(F,"+durata+")")))
                for film in listafilm:
                    print(film)
            if scelta == '7':
                nomefilm = str(input("inserisci il nome del film: ")).lower()
                print(kb.query(pl.Expr("sala("+nomefilm+",S)"))[0])
            if scelta == '8':
                nomeaddetto = str(input("inserisci il nome dell'addetto: ")).lower()
                print(kb.query(pl.Expr("addetto(S,"+nomeaddetto+")"))[0])