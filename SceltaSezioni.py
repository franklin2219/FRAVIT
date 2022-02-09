import pandas as pd
from sklearn.tree import DecisionTreeClassifier


class ScegliSezioni:

    model = DecisionTreeClassifier()

    def __init__(self):
        film = pd.read_csv('dataset_completo.csv', delimiter=";")
        x = film[["humor", "ritmo", "impegno", "tensione"]]
        y = film.sezione
        y = y.astype('int')
        x = x.astype('int')
        self.model.fit(x.values, y.values)

    @classmethod
    def inseriscivalori(cls, film):
        pred_x = [[film.humor, film.ritmo, film.impegno, film.tensione]]
        pred_y = cls.model.predict(pred_x)
        pred_y = int(pred_y)
        sezione = ""
        if pred_y == 1:
            sezione = "humor"
        elif pred_y == 2:
            sezione = "ritmo"
        elif pred_y == 3:
            sezione = "impegno"
        elif pred_y == 4:
            sezione = "tensione"
        print("Il film o la serie TV dovranno esser riposti nella sezione :", sezione)
