#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Othello, o Reversi (https://en.wikipedia.org/wiki/Reversi), è un gioco da tavolo
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

Si deve scrivere una funzione dumbothello(filename) che legga da un file di testo
indicato dalla stringa filename una configurazione della scacchiera e,
seguendo le regole di Dumbothello, generi ricorsivamente l'albero di gioco completo
delle possibili evoluzioni della partita, in modo tale che ogni foglia dell'albero
sia una configurazione da cui non sia più possibile effettuare alcuna mossa.

La configurazione inziale della scacchiera nel file è rappresentata riga per
riga nel file. Una lettera "B" identifica una pedina del nero, una "W" una
pedina del bianco e il carattere "." una casella vuota. Le lettere sono
separate da uno o più caratteri di spaziatura.

In particolare, la funzione dumbothello restituirà una tripla (a, b, c), in cui:
- a è il numero totale di evoluzioni che terminano con una vittoria del nero;
- b è il numero totale di evoluzioni che terminano con una vittoria del bianco;
- c è il numero totale di evoluzioni che terminano con un pari.

Ad esempio, dato in input un file di testo contenente la scacchiera:
. . W W
. . B B
W W W B
W B B W

La funzione ritornerà la tripla:
(2, 16, 0)

ATTENZIONE: la funzione dumbothello o qualche altra 
funzione usata per la soluzione deve essere ricorsiva.

'''


def fill_table(table: list[list], black_plays: bool):
    empty_pos = []
    for r, row in enumerate(table):
        for c, col in enumerate(row):
            if table[r][c] == ".":
                empty_pos.append([r, c])

    print(*table, sep="\n", end="\n\n")
    if not empty_pos:
        return

    neighbors = [(0, 1),  # E
                 (-1, 1),  # NE
                 (-1, 0),  # N
                 (-1, -1),  # NW
                 (0, -1),  # W
                 (1, -1),  # SW
                 (1, 0),  # S
                 (1, 1),  # SE
                 ]

    r, c = empty_pos[0][0], empty_pos[0][1]
    table[r][c] = "B" if black_plays else "W"
    change_neighbour_recursive(table, neighbors, len(table), len(table[0]), r, c, black_plays)
    return fill_table(table, not black_plays)


def change_neighbour_recursive(table, neighbours, H, W, r, c, black_plays):
    if not neighbours:
        return
    first = neighbours[0]
    to_check_r, to_check_c = (r + first[0]) % H, (c + first[1]) % W
    to_check = table[to_check_r][to_check_c]
    if to_check != ".":
        if to_check == "W" and black_plays:
            table[to_check_r][to_check_c] = "B"
        elif to_check == "B" and not black_plays:
            table[to_check_r][to_check_c] = "W"

    return change_neighbour_recursive(table, neighbours[1:], H, W, r, c, black_plays)


def dumbothello(filename: str) -> tuple[int, int, int]:
    table = []

    with open(filename) as f:
        for line in f.readlines():
            table.append(line.split())

    # fill_table(table, black_plays=True)

    endings = [0, 0, 0]

    play(table, endings=endings)
    # print(table)
    return tuple(endings)


def play(start_table, endings, free_pos=None, table=None, black_turn=True):
    if not table:
        table = [[col for col in row] for row in start_table]
    elif not any("." in row for row in table):
        num_W = sum([col.count("W") for row in table for col in row])
        num_B = sum([col.count("B") for row in table for col in row])
        if num_B > num_W:
            endings[0] += 1
        elif num_B < num_W:
            endings[1] += 1
        else:
            endings[2] += 1
        print(*table, sep="\n", end="\n\n")
        return table
    if not free_pos:
        free_pos = []
        for r, row in enumerate(table):
            for c, col in enumerate(row):
                if col == ".":
                    free_pos.append([r, c])
    neighbors = [(0, 1),  # E
                 (-1, 1),  # NE
                 (-1, 0),  # N
                 (-1, -1),  # NW
                 (0, -1),  # W
                 (1, -1),  # SW
                 (1, 0),  # S
                 (1, 1),  # SE
                 ]
    for dot in free_pos:
        r, c = free_pos[0][0], free_pos[0][1]
        table[r][c] = "B" if black_turn else "W"
        change_neighbour_recursive(table, neighbors, len(table), len(table[0]), r, c, black_turn)
        play(start_table, endings, free_pos[1:], table, not black_turn)


if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
