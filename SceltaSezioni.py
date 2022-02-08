import pandas as pd
from statistics import mean
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score

class ScegliSezioni:

    model = DecisionTreeClassifier()

    def __init__(self):
        film = pd.read_csv('dataset_completo.csv', delimiter=";")
        x = film[["humor","ritmo","impegno","tensione"]]
        y = film.sezione
        y = y.astype('int')
        x = x.astype('int')
        self.model.fit(x.values, y.values)
        #loo = LeaveOneOut()
        #result = cross_val_score(modello, x, y, scoring='accuracy', cv=loo)

    @classmethod
    def inseriscivalori(cls,film):
        pred_x = [[film.humor , film.ritmo , film.impegno , film.tensione]]
        pred_y = cls.model.predict(pred_x)
        print(pred_y)

''' 
    @classmethod
    def accuratezza(cls):
        print("L'accuratezza del sistema è: %.3f" % mean(result))
        # print("{}".format(result))
'''