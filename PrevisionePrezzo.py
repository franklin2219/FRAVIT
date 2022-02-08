import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn import metrics
from sklearn.neural_network._multilayer_perceptron import MLPClassifier


class PrevisionePrezzo:
    model = MLPClassifier()
    film = pd.read_csv("dataset_completo.csv", delimiter=";")

    def __init__(self):
        # divido il dataset in dati da usare per addestarre(x), e dati da predire(y)
        y = self.film.prezzo
        x = self.film[["voto_completo", "anno_completo", "durata_completa"]]
        # definisco che sia x che y non sono interi
        y = y.astype('int')
        x = x.astype('int')

        # divido x e y in modo da avere una parte per il training e una per il test
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

        # qui il modello apprende da solo
        self.model.fit(x_train, y_train)
        # effettuo predizione sui dati
        p_train = self.model.predict(x_train)  # p_train contiene le predizioni(y) sui dati x di training
        p_test = self.model.predict(x_test)  # p_test contiene le predizioni(y) sui dati x di test

        # calcolo accuratezza del sistema
        print("+------------------------------------------------------------------+")
        print("+                DATI SULLE PREDIZIONI                             +")
        print("+------------------------------------------------------------------+")
        print(f'+ L\'accuratezza reale sulle predizioni fatte e\' di : {metrics.balanced_accuracy_score(y_test, p_test)}')

        # calcolo errori
        mae_train = mean_absolute_error(y_train, p_train)
        mae_test = mean_absolute_error(y_test, p_test)

        print('+ MAE sul test set :', mae_test)
        print('+ MAE sul train set :', mae_train)
        print("+------------------------------------------------------------------+\n\n")

    @classmethod
    def prediciprezzo(cls, filminserito):
        pred_x = pd.DataFrame(data={"voto_completo": [filminserito.peso_voto],
                                    "anno_completo": [filminserito.peso_anno],
                                    "durata_completa": [filminserito.peso_durata]})
        pred_y = cls.model.predict(pred_x)
        print("Il prezzo per il film e' di : ",pred_y,"euro")
