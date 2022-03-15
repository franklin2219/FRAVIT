import pytholog as pl

class ControllaConvenienza:
    def convenienza(cls,voto,prezzo):
        kb = pl.KnowledgeBase("convenienza")

        kb(["conviene(conviene,P) :- voto(P) > "+prezzo,
           "voto("+voto+")"])

        if(kb.query(pl.Expr(f"conviene(conviene,P)"))[0] == 'Yes'):
            print("Conviene!")