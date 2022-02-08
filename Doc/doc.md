# Relazione tecnica

### Indice

1. [Introduzione](#Introduzione)
2. [Requisiti funzionali](#Requisiti-funzionali)
3. [Manuale utente](#Manuale-utente)
4. [Scelte progettuali](#Scelte-progettuali)
5. [Implementazioni future](#Implementazioni-future)
6. [Processo di sviluppo e organizzazione del lavoro](#Processo-di-sviluppo-e-organizzazione-del-lavoro)
7. [Conclusioni](#Conclusioni)

## **Introduzione**

Questo documento ha il compito di illustrare l’utilizzo della prima versione dell’applicazione **FRAVIT**.

L'applicativo software è stato sviluppato dal gruppo composto da: 

* **[Francesco Sasso](https://github.com/franklin2219)** (Matricola: 715742)
* **[Vito Musco](https://github.com/VitoMusco)** (Matricola: 724569)

Il nome dell'applicativo sono le iniziali del nome dei membri del gruppo.

L'assistente virtuale intelligente **FRAVIT** nasce con lo scopo di aiutare i negozi locali che si occupano della vendita
di film e serie TV in DVD, nel comprendere quale debba essere il prezzo,nel suggerire un determinato film o una serire TV
ai clienti che ne fanno richiesta e nel comprendere un nuovo film o serie TV in quale sezione del negozio debba essere posizionato.
(Suddivisi in base alle caratteristiche del film o della serie TV)

Si è scelto di utilizzare un dataset già preesistente in rete, in modo tale da poter utilizzare come base di conoscenza 
dei dati sufficienti per ottenere gli obiettivi stabiliti.
Sono state effettuate delle modifiche a tale dataset come l'inserimento delle colonne "voto_completo","durata_completa",
"anno_completo","genere_convertito" utilizzate per fornire degli esempi di prezzi dei film presenti nel dataset e per 
effettuare il suggerimento del film al cliente.


[Torna all'inizio](#Indice)

## **Requisiti funzionali**

Per avviare correttamente il programma è necessario installare:

* 'numpy' tramite il comando da terminale ```pip install numpy``` per la predizione;
* 'pandas' tramite il comando da terminale ```pip install pandas``` per il classificatore;
* 'sklearn.tree' tramite il comando da terminale ```pip install scikit-learn``` per il classificatore;
* 'matplolib' tramite il comando da terminale ``` pip install -U matplotlib``` per il classificatore;


[Torna all'inizio](#Indice)

## **Manuale utente**

La prima volta che si importa il progetto, la compilazione potrebbe richiedere qualche secondo in più!

Quando il programma sarà avviato verrà visualizzato la schermata principale a linea di comando:

<center><img src = "photo/Schermata_principale.png"></center>

Se avviato correttammente da questo momento in poi si potranno utilizzare i seguenti comandi:

* ```Inserisci nuovo Film``` - comando che viene suggerito dal banner iniziale, e che se invocato permette di inserire i dati di un nuovo film che dovrà essere inserito nel negozio in modo tale da comprendere quale sarà il suo prezzo.
* ```Suggerisci Film``` - comando che viene suggerito dal banner iniziale, e che se invocato permette di inserire i dati relativi ai gusti del cliente permettendo a FRAVIT di suggerire uno tra i film presenti nel dataset e che rispetteranno i gusti forniti.
* ```Insirisci Film in una sezione``` - comando che viene suggerito dal banner iniziale, e che permette di inserire i dati relativi al film/serieTV di cui si vuole comprendere la sezione e si otterrà la sezione nella quale quel determinato film/serieTV deve essere posto.
* ```Esci``` - comando per terminare l'applicazione.

Una volta terminato correttamente il programma, verrà visualizzato a linea di comando il seguente messaggio:

<center>

```A presto!```

</center>

In seguito, l'applicazione verrà chiusa.
 
Vengono gestiti tutti i casi in cui l'utente inserisce un input errato!

Di seguito un esempio di interazione con il sistema nel caso si voglia comprendere il prezzo di un nuovo film/serieTV: 

<center><img src = "photo/Esempio_interazione.png"></center>

Di seguito un esempio di interazione con il sistema nel caso si voglia suggerire film/serieTV:

<center><img src = "photo/Esempio_interazione.png"></center>

Di seguito un esempio di interazione con il sistema nel caso si voglia inserire un nuovo film/serieTV in una sezione:

<center><img src = "photo/Esempio_interazione.png"></center>

[Torna all'inizio](#Indice)

## **Scelte progettuali**

Nel nostro applicativo software si è scelto di utilizzare:

* Una [base di conoscenza](https://it.wikipedia.org/wiki/Base_di_conoscenza), contente più di 207408 tra Film e SerieTv alla quale però sono state aggiunte informazioni necessarie per l'utilizzo dell'applicazione come:
  - ```genere_convertito``` utilizzato per la conversione del genere di un film/serie TV in valori numerici utili agli scopi progettuali (da 1 a 27)
  - ```voto_completo``` utilizzato per rappresentare il voto fornito dall'utente in un valore numerico utile agli scopi progettuali (da 1 a 4)
  - ```durata_completa``` utilizzata per rappresentare la durata del film/serie TV con dei valori numerici utili agli scopi progettuali (da 1 a 3)
  - ```anno_completo``` utilizzato per rappresentare l'anno di pubblicazione del film/serie TV con dei valori numerici utili agli scopi progettuali (da 1 a 4)
* Una [rete neurale](https://it.wikipedia.org/wiki/Rete_neurale_artificiale) in grado di predire il prezzo di un nuovo film/serieTV in base alle informazioni che gli verranno fornite. Per predire il prezzo analizzerà il voto ricevuto, l'anno di pubblicazione e la durata del film/serie TV.
* Un [K-nearest_neighbors](https://it.wikipedia.org/wiki/K-nearest_neighbors) in grado di suggerire un determinato film o una serieTV al cliente in base alle informazioni fornite in input che rappresenteranno le proprietà del film che si vorrà vedere.
Verrà richiesto il genere di film che si intende vedere,il periodo cinematografico che si preferisce vedere ed i livelli di humor,tensione,ritmo,erotismo,impegno richiesti.
* Un [albero di decisione](https://it.wikipedia.org/wiki/Albero_di_decisione) in grado di far comprendere in quale sezione del negozio dovrà essere posto un determinato film o una serie TV, in base alle caratteristiche inserite in input.
  - sezione 1 --> film o serie TV con maggior *humor*.
  - sezione 2 --> film o serie TV con maggior *ritmo*.
  - sezione 3 --> film o serie TV con maggior *impegno*.
  - sezione 4 --> film o serie TV con maggior *tensione*.
  - sezione 5 --> film o serie TV con maggior *erotismo*.
* [Precision e Recall](https://it.wikipedia.org/wiki/Precisione_e_recupero) come metriche di valutazione del sistema con l'utilizzo di una matrice di confusione.
<center><img src = "photo/ConfusionMatrix.png"></center>

### **Base di Conoscenza**

Abbiamo dotato il nostro applicativo di un menù che permetterà di interagire con le informazioni presenti nel dataset utilizzando i seguenti comandi:

* ```Visualizza Film/Serie TV```;
* ```Visualizza Generi presenti```;
* ```Visualizza Ultimo film suggerito```;
* ```Visualizza Ultimo film con il relativo prezzo ```;
* ```Torna indietro```;

### **Classificatore**

Il programma è stato dotato di una funzione che sfrutta un classificatore per determinare la classe salariale a cui apparterrà l'utente una volta assunto.
Abbiamo utilizzato un [file CSV](https://it.wikipedia.org/wiki/Comma-separated_values) per addestrare il nostro classificatore. Le informazioni che l'utente deve inserire sono:

* ```Age```;
* ```Sex```;
* ```Years Experience```;
* ```Salary```.

Ad ogni campo sono stati associati i seguenti valori:

* Per l'età, un intero;
* Per il sesso, sono stati mappati i valori nella seguente modalità:
<center>

| Sex = Male | Sex = Female |
|---|--------------|
| 0 | 1            | 

</center>

* Per l'esperienza in azienda, un float;
* Per il salario annuale, un range di valori.

Il risultato della funzione ```calcola_salario``` sarà un range di salario a cui l'utente potrà ambire. Fornito l'esempio, l'algoritmo restituisce la classe a cui potrebbe appertenere. Le classi possibili sono:

* ```20000-30000€```;
* ```30000-40000€```;
* ```40000-50000€```;
* ```50000-60000€```;
* ```60000-70000€```.

Inoltre con il comando ```accuratezza_classificatore``` sarà restituita l'accuratezza del classificatore, calcolata con
l'algoritmo 'leave-one-out cross validation'. Questo algoritmo è stato utilizzato perche il dataset essendo stato scritto da noi, ha pochi esempi, quindi per valutare un dataset con pochi elementi è opportuno utilizzare questo algoritmo.
### **Rete Bayesiana**

Nel nostro applicativo è stata implementata una funzione che sfrutta una Rete Bayesiana. Questa è in grado di predire la percentuale di possibilità di assunzione dell'utente nell'azienda. L'assistente, infatti, ponendo delle domande 
all'utente, calcolerà un float compreso tra 0 e 1, che moltiplicato per 100 darà come risultato la percentuale di possibilità di assunzione. In base alla percentuale restituita:
* se la percentuale è ```< 26%``` la predizione rientrerà nella fascia ```bassa```;
* se la percentuale è ```< 40%``` la predizione rientrerà nella fascia ```medio-bassa```;
* se la percentuale è ```< 50%``` la predizione rientrerà nella fascia ```media```;
* se la percentuale è ```< 70%``` la predizione rientrerà nella fascia ```medio-alta```;
* se la percentuale è ```>= 70%``` la predizione rientrerà nella fascia ```alta```.

Ogni risposta è pesata differentemente e queste percentuali sono determinate da:

* **Titolo**: titolo di studio conseguito dall'utente;  
* **Esperienza Pregressa**: se l'utente ha mai lavorato in un'azienda;
* **Valore Personale**: padre di ```Titolo``` e di ```Esperienza pregressa```;
* **Passione Informatica**: se l'utente è appassionato al mondo informatico;
* **Sviluppo Web**: preferenza tra programmazione [Back End](https://www.geekandjob.com/carriera/back-end-developer) e programmazione [Front End](https://www.a-sapiens.it/informatica/risorse/come-diventare-front-end-developer/);
* **Valore Informatico**: padre di ```Passione Informatica``` e di ```Sviluppo Web```;
* **Punteggio Personale**: padre di ```Valore Personale``` e di ```Valore Informatico```;
* **Conoscenza Java**: se l'utente conosce il linguaggio di programmazione [Java](https://it.wikipedia.org/wiki/Java_(linguaggio_di_programmazione));
* **Conoscenza Python**: se l'utente conosce il linguaggio di programmazione [Python](https://it.wikipedia.org/wiki/Python)
* **Conoscenza Linguaggi**: padre di ```Conoscenza Java``` e di ```Conoscenza Python```;
* **Conoscenza MySQL**: se l'utente conosce il linguaggio di riferimento per database relazionali [MySQL](https://it.wikipedia.org/wiki/MySQL);
* **Conoscenza MongoDB**: se l'utente conosce il linguaggio di riferimento per database non relazionali [MongoDB](https://it.wikipedia.org/wiki/MongoDB);
* **Conoscenza DB**: padre di ```Conoscenza MySQL``` e di ```Conoscenza MongoDB```;
* **Valore Lavorativo**: padre di ```Conoscenza Linguaggi``` e di ```Conoscenza DB```;
* **Previsione Assunzione**: padre di ```Punteggio Personale``` e di ```Valore Lavorativo```;


**ESEMPI RETE BAYESIANA**:
---
* P(titoloStudio = laurea) = 0.70                 
* P(titoloStudio = diploma) = 0.25
* P(titoloStudio = titolo inferiore) = 0.05

* P(esperienzaPregressa = si) = 0.85
* P(esperienzaPregressa = no) = 0.15


* P(ValorePersonale=ottimo | titoloStudio = laurea ∧ esperienzaPregressa= si) = 0.98
* P(ValorePersonale=scarso | titoloStudio = laurea ∧ esperienzaPregressa= si) = 0.02
* P(ValorePersonale=ottimo | titoloStudio = laurea ∧ esperienzaPregressa= no) = 0.75
* P(ValorePersonale=scarso | titoloStudio = laurea ∧ esperienzaPregressa= no) = 0.25
* P(ValorePersonale=ottimo | titoloStudio = diploma ∧ esperienzaPregressa= si) = 0.6
* P(ValorePersonale=scarso | titoloStudio = diploma ∧ esperienzaPregressa= si) = 0.4
* P(ValorePersonale=ottimo | titoloStudio = diploma ∧ esperienzaPregressa= no) = 0.51
* P(ValorePersonale=scarso | titoloStudio = diploma ∧ esperienzaPregressa= no) = 0.49
* P(ValorePersonale=ottimo | titoloStudio = titolo inferiore ∧ esperienzaPregressa= si) = 0.15
* P(ValorePersonale=scarso | titoloStudio = titolo inferiore ∧ esperienzaPregressa= si) = 0.85
* P(ValorePersonale=ottimo | titoloStudio = titolo inferiore ∧ esperienzaPregressa= no) = 0.05
* P(ValorePersonale=scarso | titoloStudio = titolo inferiore ∧ esperienzaPregressa= no) = 0.95


* P(passioneInformatica = si) = 0.85
* P(passioneInformatica = no) = 0.15

* P(sviluppoWeb = back end) = 0.71
* P(sviluppoWeb = front end) = 0.29


* P(ValoreInformatico = ottimo | passioneInformatica = si ∧ sviluppoWeb = back end) = 0.8
* P(ValoreInformatico = scarso | passioneInformatica = si ∧ sviluppoWeb = back end) = 0.2
* P(ValoreInformatico = ottimo | passioneInformatica = si ∧ sviluppoWeb = front end) = 0.73
* P(ValoreInformatico = scarso | passioneInformatica = si ∧ sviluppoWeb = front end) = 0.27
* P(ValoreInformatico = ottimo | passioneInformatica = no ∧ sviluppoWeb = back end) = 0.33
* P(ValoreInformatico = scarso | passioneInformatica = no ∧ sviluppoWeb = back end) = 0.67
* P(ValoreInformatico = ottimo | passioneInformatica = no ∧ sviluppoWeb = front end) = 0.02
* P(ValoreInformatico = scarso | passioneInformatica = no ∧ sviluppoWeb = front end) = 0.98

[Torna all'inizio](#Indice)

## **Implementazioni future**

In futuro, alcune feature che potrebbero essere implementate sono:

1. Inserimento GUI;
2. Progetti con richieste dettagliate;
3. Controlli sul numero di assunzioni;
4. Consigli sull'assunzione di determinato personale in base ai tipi di progetti;
5. Stima del tempo per il completamento di un progetto;
6. Richiesta di particolari dipendenti in base alle tecnologie utilizzate all'interno di un progetto.
7. Differenziare i comandi disponibili in base al tipo di utente che accede all'assistente.

[Torna all'inizio](#Indice)

## **Processo di sviluppo e organizzazione del lavoro**

Il progetto è stato sviluppato a partire da Dicembre 2021 fino a metà Gennaio 2022 completamente in remoto.

## **Piattaforme di comunicazione**

Per la comunicazione, il nostro gruppo, ha adottato due piattaforme:

* **[Microsoft Teams](https://discord.com/brand-new)**
* **[Whatsapp](https://www.whatsapp.com/?lang=it)**

La prima è stata scelta poichè una piattaforma a tutti i membri del gruppo familiare, la quale permetteva di organizzare videoconferenze e di condividere lo schermo. Ciò è stato molto utile nel momento in cui sorgevano difficoltà in quanto si poteva risolvere il problema tutti insieme.

<center><img src = "../Doc/photo/teams.png"></center>

La seconda è stata scelta poichè, essendo anche questa familiare, era il mezzo di comunicazione più immediata. Tramite questa piattaforma, è stato possibile confrontarsi durante lo sviluppo, decidere i giorni e gli orari per i nostri meeting e tenersi contatto.

<center><img src = "../Doc/photo/whatsappIcon.png"></center>

[Torna all'inizio](#Indice)

## **Conclusioni**

Come detto in precedenza, riteniamo che questo progetto sia stato un importante banco di prova. Nonostante le difficoltà siamo riusciti comunque a centrare gli obiettivi stabiliti e a trarre il meglio da questa esperienza formativa.

Rigraziamo per l'attenzione. 

<center>

Lo staff, **[FARIDA](https://github.com/RickNewere/FARIDA.git)**

</center>

[Torna all'inizio](#Indice)