# Algorithm
  - [italiano](#ita)
  - [english](#en)

## Ita
Othello, o [Reversi](https://en.wikipedia.org/wiki/Reversi), è un gioco da tavolo
giocato da due giocatori su una scacchiera 8x8. Pur avendo regole
relativamente semplici, Othello è un gioco di notevole profondità strategica.
In questo esercizio bisognerà simulare una versione semplificata di othello,
chiamata Dumbothello, in cui un giocatore cattura le pedine dell'avversario in
prossimità della propria pedina appena giocata.
Ecco le regole di Dumbothello:
- ogni giocatore ha un colore associato: bianco, nero;
- il giocatore con il nero è sempre il primo a giocare;
- a turno, ogni giocatore deve mettere una pedina del suo colore in modo tale
  da catturare una o più pedine avversarie;
- catturare una o più pedine avversarie vuol dire che la pedina giocata dal
  giocatore trasforma nel colore del giocatore tutte le pedine avversarie
  direttamente adiacenti, in una qualunque direzione orizzontale, verticale o diagonale;
- dopo aver giocato la propria pedina, le pedine avversarie catturate cambiano
  tutte colore e diventano dello stesso colore del giocatore che ha appena giocato;
- quando il giocatore di turno non può aggiungere ulteriori pedine in gioco,
  la partita termina. Vince il giocatore che ha più pedine sulla scacchiera
  oppure avviene un pareggio se il numero di pedine dei due giocatori è uguale;
- il giocatore di turno non può aggiungere ulteriori pedine se non ha modo di
  catturare nessuna pedina avversaria con nessuna mossa, oppure non ci sono
  più caselle libere sulla scacchiera.

Si deve scrivere una funzione `dumbothello(filename)` che legga da un file di testo
indicato dalla stringa filename una configurazione della scacchiera e,
seguendo le regole di Dumbothello, generi ricorsivamente l'albero di gioco completo
delle possibili evoluzioni della partita, in modo tale che ogni foglia dell'albero
sia una configurazione da cui non sia più possibile effettuare alcuna mossa.

La configurazione inziale della scacchiera nel file è rappresentata riga per
riga nel file. Una lettera `B` identifica una pedina del nero, una `W` una
pedina del bianco e il carattere `.` una casella vuota. Le lettere sono
separate da uno o più caratteri di spaziatura.

In particolare, la funzione dumbothello restituirà una tripla `(a, b, c)`, in cui:
- `a` è il numero totale di evoluzioni che terminano con una vittoria del nero;
- `b` è il numero totale di evoluzioni che terminano con una vittoria del bianco;
- `c` è il numero totale di evoluzioni che terminano con un pari.

Ad esempio, dato in input un file di testo contenente la scacchiera:

|     |     |     |     |
|-----|-----|-----|-----|
| .   | .   | W   | W   |
| .   | .   | B   | B   |
| W   | W   | W   | B   |
| W   | B   | B   | W   |

La funzione ritornerà la tripla:

`(2, 16, 0)`

**ATTENZIONE**: la funzione `dumbothello` o qualche altra 
funzione usata per la soluzione deve essere *ricorsiva*.

## En
Othello, or [Reversi](https://en.wikipedia.org/wiki/Reversi), is a board game
played by two players, playing "disks" of different colors an 8x8 board.
Despite having relatively simple rules, Othello is a game of high strategic depth.
In this homework you will need to simulate a simplified version of othello,
called Dumbothello, in which each player can capture the opponent's disks
by playing a new disk on an adjacent empty cell.
The rules of Dumbothello are:
- each player has an associated color: white, black;
- the player with black is always the first to play;
- in turn, each player must place a disk of their color in such a way
  to capture one or more opponent's disks;
- capturing one or more opponent's disks means that the disk played by the
  player changes into the player's color all the directly adjacent opponent's disks,
  in any horizontal, vertical or diagonal direction;
- after playing one's own disk, the captured opponent's disks change
  their color, and become the same color as the player who just played;
- if the player who has the turn cannot add any disk on the board,
  the game ends. The player who has the higher number of disks on the board wins
  or a tie occurs if the number of disks of the two players is equal;
- the player who has the turn cannot add any disk if there is
  no way to capture any opponent's disks with any move, or if there are no
  more free cells on the board.

Write a function `dumbothello(filename)` that reads the configuration of the
board from the text file indicated by the string "filename" and,
following the rules of Dumbothello, recursively generates the complete game tree
of the possible evolutions of the game, such that each leaf of the tree
is a configuration from which no more moves can be made.

The initial configuration of the chessboard in the file is stored line by
line in the file: letter `B` identifies a black disk, a `W` a white disk,
and the character `.` an empty cell. The letters are separated by one or
more spacing characters.

The `dumbothello` function will return a triple `(a, b, c)`, where:
- `a` is the total number of evolutions ending in a black victory;
- `b` is the total number of evolutions ending in a white victory;
- `c` is the total number of evolutions ending in a tie.

For example, given as input a text file containing the board:

|     |     |     |     |
|-----|-----|-----|-----|
| .   | .   | W   | W   |
| .   | .   | B   | B   |
| W   | W   | W   | B   |
| W   | B   | B   | W   |

The function will return the triple:
`(2, 16, 0)`

**NOTICE**: the `dumbotello` function or some other function used by it must be *recursive*.
