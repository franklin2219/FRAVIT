from User import Utente
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors._classification import KNeighborsClassifier
from sklearn.metrics import mean_absolute_error;
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from numpy import mean
from numpy import std
from sklearn import metrics
from sklearn.neural_network._multilayer_perceptron import MLPClassifier

class PrevisionePrezzo:
    if __name__ == '__main__':
        film = pd.read_csv("/Users/srancescosasso/SimulatoreNoleggioAcquisto/dataset_completo.csv",delimiter=";")

        #divido il dataset in dati da usare per addestarre(x), e dati da predire(y)
        y = film.prezzo
        x = film[["voto_completo","anno_completo","durata_completa"]]
        #definisco che sia x che y non sono interi
        y=y.astype('int')
        x=x.astype('int')

        print(x,y)

        #divido x e y in modo da avere una parte per il training e una per il test
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

        model = MLPClassifier()
        #qui il modello apprende da solo
        model.fit(x_train, y_train)
        #effettuo predizione sui dati
        p_train = model.predict(x_train)#p_train contiene le predizioni(y) sui dati x di training
        p_test = model.predict(x_test)#p_test contiene le predizioni(y) sui dati x di test

        #calcolo accuratezza del sistema
        print(f'L\'accuratezza reale sulle predizioni fatte e\' di {metrics.balanced_accuracy_score(y_test, p_test)}')

        #calcolo errori
        mae_train = mean_absolute_error(y_train, p_train)
        mae_test = mean_absolute_error(y_test, p_test)

        print('MAE test', mae_test)
        print('MAE train', mae_train)

    pass

