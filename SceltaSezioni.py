import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

class ScegliSezioni:
    film = pd.read_csv('dataset_completo.csv', delimiter=";")
    model = DecisionTreeClassifier()
    maeTRAIN=0
    maeTEST=0
    precisione=0
    richiamo=0
    accuratezza=0

    def __init__(self):
        x = self.film[["humor", "ritmo", "impegno", "tensione"]]
        y = self.film.sezione
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
        cls.precisione=precision
        cls.richiamo=recall


    @classmethod
    def datiPredizioni(cls, precision, recall, accuratezza):

        print("\n\n\n+------------------------------------------------------------------+")
        print("+                    DATI SULLE PREDIZIONI SEZIONI                 +")
        print("+------------------------------------------------------------------+")
        print("+ Precision : ",precision)
        print("+ Recall : ", recall)
        print(f"+ Accuratezza : {format(accuratezza.mean())}")
        print("+------------------------------------------------------------------+\n\n")