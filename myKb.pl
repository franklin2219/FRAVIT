:- discontiguous(i_film/4).
:- discontiguous (i_sala/3).
:- discontiguous (i_personale/3).
%-----------------------------------------------------------------------------
%Regole Film

%Mostra il titolo del film in base al genere e viceversa
film(Titolo, I_film1) :- i_film(Titolo,I_film1,_,_).
%Mostra la durata del film in base al Titolo e viceversa
durata(Film,Durata) :- i_film(Film,_,_,Durata).
%Mostra il titolo del film in base alla sala selezionata e viceversa
sala(Titolo,Sala) :- i_film(Titolo,_,Sala,_).
%Mostra l'addetto alla proiezione di una determinata sala
addetto(Sala,Addetto) :- i_sala(Sala,Addetto,_).

%-----------------------------------------------------------------------------
%Regole Dipendenti Sale

%Mostriamo i proiezionisti per quella sala

%-----------------------------------------------------------------------------

%DATI

%Immissione film

i_film(dumbo,animazione,sala1,90).
i_film(abissi,avventura,sala2,180).
i_film(assassination,azione,sala1,100).
i_film(ben_Hur,biblico,sala3,90).
i_film(bird,biografico,sala4,60).
i_film(la_crociera_del_terrore,catastrofico,sala1,130).
i_film(abbronzatissimi,commedia,sala3,90).
i_film(cineocchio,documentario,sala2,180).
i_film(accattone, drammatico,sala3,90).
i_film(alien, fantasy,sala4,100).
i_film(borsalino, gangster,sala3,60).
i_film(amarcord, grottesco,sala2,90).
i_film(bataan, guerra,sala1,180).
i_film(dracula, horror,sala4,90).
i_film(gli_argonauti, mitologico,sala3,70).

%Informazioni Addetti Proiezioni film

i_sala(sala1,vito,proiezionista).
i_personale(sala1,vito,altamura,30-09-2000).
i_sala(sala2,michele,proiezionista).
i_personale(michele,gravina,19-05-1998).
i_sala(sala3,vincenzo,proiezionista).
i_personale(vincenzo,roma,23-04-1990).
i_sala(sala4,francesco,proiezionista).
i_personale(francesco,bari,22-07-2000).
%--------------------------------------------------------------------------------
                                  
