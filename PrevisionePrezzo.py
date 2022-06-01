import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import scikitplot as sklpt
#from sklearn.neural_network._multilayer_perceptron import MLPClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors._classification import KNeighborsClassifier

class PrevisionePrezzo:
    model = KNeighborsClassifier()
    film = pd.read_csv("dataset_completo.csv", delimiter=";")
    maeTRAIN=0
    maeTEST=0
    precisione=0
    richiamo=0
    accuratezza=0

    def __init__(self):
        y = self.film.prezzo
        x = self.film[["voto_convertito", "anno_convertito", "durata_convertita"]]
        y = y.astype('int')
        x = x.astype('int')

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

        self.model.fit(x_train, y_train)

        p_train = self.model.predict(x_train)
        p_test = self.model.predict(x_test)

        self.calc_precision_recall(y_test, p_test)

        mae_train = mean_absolute_error(y_train, p_train)
        mae_test = mean_absolute_error(y_test, p_test)
        self.maeTEST=mae_test
        self.maeTRAIN=mae_train

        k=10
        kf =KFold(n_splits=k,random_state=None)
        result=cross_val_score(self.model,x,y,cv=kf,n_jobs=-1)
        self.accuratezza=result


    @classmethod
    def prediciprezzo(cls, filminserito):
        pred_x = pd.DataFrame(data={"voto_convertito": [filminserito.peso_voto],
                                    "anno_convertito": [filminserito.peso_anno],
                                    "durata_convertita": [filminserito.peso_durata]})
        pred_y = cls.model.predict(pred_x)
        print("Il prezzo per il film e' di :", int(pred_y), "euro")

    @classmethod
    def calc_precision_recall(cls, y_true, y_pred):

        y_pred = pd.Series(y_pred, index=y_true.index)

        tp = 0
        fp = 0
        fn = 0

        for i in y_true.index:
            if y_true[i] == y_pred[i]:
                tp += 1
            if y_true[i] != y_pred[i]:
                fp += 1
            if y_pred[i] == "" and y_true[i] != y_pred[i]:
                fn += 1

        try:
            precision = tp / (tp + fp)
        except:
            precision = 1

        try:
            recall = tp / (tp + fn)
        except:
            recall = 1
        sklpt.metrics.plot_confusion_matrix(y_true, y_pred)
        plt.show()
        cls.precisione=precision
        cls.richiamo=recall


    @classmethod
    def datiPredizioni(cls, precision, recall, mae_test, mae_train, accuratezza):

        print("\n\n\n+------------------------------------------------------------------+")
        print("+                      DATI SULLE PREDIZIONI SUGGERIMENTO             +")
        print("+------------------------------------------------------------------+")
        print("+ Precision : ",precision)
        print("+ Recall : ", recall)
        print(f"+ Accuratezza : {format(accuratezza.mean())}")
        print('+ MAE sul test set :', mae_test)
        print('+ MAE sul train set :', mae_train)
        print("+------------------------------------------------------------------+\n\n")

