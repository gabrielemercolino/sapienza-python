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


def calc_ending(state: list[list[str]], endings: list[int, int, int]):
    # print(*state, sep="\n", end="\n\n")
    numW = len([cell for row in state for cell in row if cell == "W"])
    numB = len([cell for row in state for cell in row if cell == "B"])
    endings[:] = [endings[0] + int(numB > numW),
                  endings[1] + int(numW > numB),
                  endings[2] + int(numB == numW)]


def check_free_pos(state: list[list[str]]):
    return any(c for row in state for c in row if c == ".")


def check_enemy_neighbors(state: list[list[str]], pos: tuple[int, int],
                          neighbors: set[tuple[int, int]], black_turn: bool):
    enemy = "W" if black_turn else "B"
    for neighbor in neighbors:
        dr, dc = pos[0] + neighbor[0], pos[1] + neighbor[1]
        if (0 <= dr < len(state)) and (0 <= dc < len(state[0])) and state[dr][dc] == enemy:
            return True
    return False


def get_free_pos(state: list[list[str]], neighbors: set[tuple[int, int]],
                 black_turn: bool) -> list[tuple[int, int]]:
    return [(r, c) for r, row in enumerate(state) for c, cell in enumerate(row) if
            cell == "." and check_enemy_neighbors(state, (r, c), neighbors, black_turn)]


def capture_enemy_neighbors(state: list[list[str]], pos: tuple[int, int],
                            neighbors: set[tuple[int, int]], black_turn: bool):
    for neighbor in neighbors:
        dr, dc = pos[0] + neighbor[0], pos[1] + neighbor[1]
        if 0 <= dr < len(state) and 0 <= dc < len(state[0]) and state[dr][dc] != ".":
            state[dr][dc] = "B" if black_turn else "W"


def play(state: list[list[str]], endings: list[int, int, int],
         neighbors: set[tuple[int, int]], black_turn: bool):
    if not check_free_pos(state):
        calc_ending(state, endings)
        return
    all_free_cells = get_free_pos(state, neighbors, black_turn)
    if not all_free_cells:
        calc_ending(state, endings)
        return
    for (r, c) in all_free_cells:
        new_state = [list(row) for row in state]
        new_state[r][c] = "B" if black_turn else "W"
        capture_enemy_neighbors(new_state, (r, c), neighbors, black_turn)
        play(new_state, endings, neighbors, not black_turn)


def dumbothello(filename: str) -> tuple[int, int, int]:
    neighbors: set[tuple[int, int]] = {
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    }
    table = []

    with open(filename) as f:
        table.extend(line.split() for line in f)

    endings = [0, 0, 0]

    play(table, endings, neighbors, black_turn=True)

    return tuple(endings)


if __name__ == "__main__":
    tests = [
        ('boards/01.txt', (2, 16, 0)),
        ('boards/02.txt', (78, 2, 16)),
        ('boards/03.txt', (1574, 2700, 1926)),
        ('boards/04.txt', (1538, 2292, 1502)),
        ('boards/05.txt', (70, 48, 0)),
        ('boards/06.txt', (190, 274, 104)),
        ('boards/07.txt', (60, 25, 13)),
        ('boards/08.txt', (2742, 1204, 794)),
        ('boards/09.txt', (0, 16, 15))
    ]
    for i, (filename, expected) in enumerate(tests):
        R = dumbothello(filename)
        print(f'test n {i}')
        print(f'\tresult:   {R}')
        print(f'\texpected: {expected}\n')
