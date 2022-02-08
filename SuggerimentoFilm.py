import pandas as pd
from sklearn.neighbors._classification import KNeighborsClassifier


class SuggerisciFilm:
    def __init__(self, filminserito):
        model = KNeighborsClassifier()
        film = pd.read_csv("dataset_completo.csv", delimiter=";")

        y = film.titolo_italiano
        x = film[["humor", "ritmo", "impegno", "tensione", "genere_convertito", "anno_completo"]]

        # definisco che sia x che y non sono interi
        y = y.astype('string')
        x = x.astype('int')

        # divido x e y in modo da avere una parte per il training e una per il test
        # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

        # qui il modello apprende da solo
        model.fit(x, y)
        # effettuo predizione sui dati
        # p_train = model.predict(x)#p_train contiene le predizioni(y) sui dati x di training
        # p_test = model.predict(x)#p_test contiene le predizioni(y) sui dati x di test

        pred_x = pd.DataFrame(data={"humor": [filminserito.humor], "ritmo": [filminserito.ritmo],
                                    "impegno": [filminserito.impegno], "tensione": [filminserito.tensione],
                                    "genere_convertito": [filminserito.genere_numerico],
                                    "anno_completo": [filminserito.peso_anno]})
        pred_y = model.predict(pred_x)
        print("Il film che ti suggeriamo e': ", pred_y)
