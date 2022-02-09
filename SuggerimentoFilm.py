import pandas as pd
from sklearn.neighbors._classification import KNeighborsClassifier


class SuggerisciFilm:
    def __init__(self, filminserito):
        model = KNeighborsClassifier()
        film = pd.read_csv("dataset_completo.csv", delimiter=";")

        y = film.titolo_italiano
        x = film[["humor", "ritmo", "impegno", "tensione", "genere_convertito", "anno_completo"]]
        y = y.astype('string')
        x = x.astype('int')
        model.fit(x, y)

        pred_x = pd.DataFrame(data={"humor": [filminserito.humor], "ritmo": [filminserito.ritmo],
                                    "impegno": [filminserito.impegno], "tensione": [filminserito.tensione],
                                    "genere_convertito": [filminserito.genere_numerico],
                                    "anno_completo": [filminserito.peso_anno]})
        pred_y = model.predict(pred_x)
        print("Il film che ti suggeriamo e':", pred_y)
