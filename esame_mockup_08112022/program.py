################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE SUBITO QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome = "Gabriele"
cognome = "Mercolino"
matricola = "2046313"

################################################################################
################################################################################
################################################################################
# SUGGERIMENTI PER IL DEBUG
#   per eseguire solo parte dei test commentare le righe 288-292 alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py
################################################################################
################################################################################
################################################################################

'''
Esercizio 1: 6 punti

Sia data una tabella rappresentata come lista di dizionari.  Ciascuna
colonna della tabella è individuata dal suo nome.  Ciascun dizionario
contenuto nella lista ha le stesse chiavi, che sono i nomi delle
colonne della tabella.  I valori possono essere stringhe, interi o
float.

Esempio: la tabella
    Nome    Cognome     Telefono    Indirizzo
    Andrea  Sterbini    137487468   via del Pero 3
    Gianni  Pierini     764817689   via degli Angeli 17

Corrisponde alla lista di dizionari
[   { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
    { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
    { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
]

Si progetti la funzione es1(tabella, colonne, elimina) che riceve come argomenti:
    - tabella: una tabella rappresentata come lista di dizionari
    - colonne: una lista di nomi di colonne rispetto alle quali ordinare la tabella
    - elimina: una lista di nomi di colonne che vanno completamente eliminate

e che torna come risultato il numero di colonne eliminate in modo che
le sue righe siano ordinate in ordine crescente relativamente al
sottoinsieme di valori presenti nelle colonne indicate.  Ed inoltre
tutte le colonne indicate nella lista 'elimina' vallo eliminate dai
dizionari.

Esempio: se colonne=['Nome', 'Cognome'] e elimina=['Telefono'] la tabella deve diventare
[   { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Indirizzo': 'via del Pero 3' },
    { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Indirizzo': 'via degli Angeli 17' },
    { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Indirizzo': 'via degli Angeli 14' }
]

Esempio: se colonne=['Telefono', 'Nome', 'Indirizzo'] la tabella deve diventare
[   { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
    { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
    { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
]

NOTA: se colonne=[] la tabella deve rimanere invariata.
NOTA: se elimina=[] non deve essere eliminata nessuna colonna.
'''


def ex1(tabella, colonne, elimina):
    # Nota 1: Prima di scrivere codice provate a risolvere il problema su carta
    # e a descrivere l'algoritmo di risoluzione a parole.
    # Nota 2: se il codice diventa complesso, spezzatelo in sotto funzioni!
    # Scrivi qui il tuo codice

    tabella.sort(key=lambda diz: [diz[c] for c in colonne if c in diz])
    #tabella[:] = [diz.pop(key) for diz in tabella for key in elimina if key in diz]
    for diz in tabella:
        for key in elimina:
            if key in diz:
                del diz[key]
    return len(elimina)

# ----------------------------------- EX.2 ----------------------------------- #


""" Es 2: 6 punti

Parte 1)
E' dato in ingresso un dizionario D che ha come chiave un intero
e come valore una lista di interi con ripetizioni.

D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}

Si implementi la funzione ex1(D, list_rm) che restituisca il dizionario
"inverso" W in cui:
 - esiste una chiave per ogni intero presente nelle liste dei valori di D
 - i nuovi valori di W sono le chiavi di D che hanno generato la
   chiave di W, ripetute per quante volte la chiave di W è presente nel
   valore delle chiavi di D.

Il dizionario inverso W deve avere ciascuna lista associata alla
chiave, ordinata in modo che prima vi siano i numeri pari e poi i
dispari; a sua volta i pari sono ordinati in maniera decrescente e i
dispari in maniera crescente.

L'esempio sopra deve restituire:

    W = {6: [2], 4: [2, 1, 1, 1], 2: [1], 3: [2, 1], 5: [2]}

Parte 2) Si estenda la funzione ex1(D, list_rm) in modo che siano
cancellati dal dizionario D in maniera distruttiva tutti gli interi nei
valori di D che compaiono in list_rm. Se dopo aver rimosso i valori una
lista in D è vuota, allora la chiave corrispondente deve essere cancellata
dal dizionario.

Esempio: se D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}
         e list_rm = [4, 3, 2, 5]
         D deve essere trasformato in maniera distruttiva in
         {2: [6]} in quanto sono tolti tutti i valori tranne il 6
         e D non contiene più la lista vuota associata alla chiave 1.
"""


def order(n):
    if n % 2 == 0:
        return [0, -n]
    return [1, n]


def ex2(D: dict[int, list], list_rm):
    # Nota 1: Prima di scrivere codice provate a risolvere il problema su carta
    # e a descrivere l'algoritmo di risoluzione a parole.
    # Nota 2: se il codice diventa complesso, spezzatelo in sotto funzioni!
    # Scrivi qui il tuo codice
    W = {}
    for key in D:
        for num in D[key]:
            W[num] = W.get(num, []) + [key]

    for el in W:
        W[el].sort(key=order)

    for key in D:
        for n in list_rm:
            while n in D[key]:
                D[key].remove(n)
    for key in list(D.keys()):
        if len(D[key]) == 0:
            del D[key]
    return W


if __name__ == '__main__':
    test_dict = {1: [2, 3], 2: [4, 5]}
    print(ex2(test_dict, []))
