#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc_ending(state: list[list[str]], endings: list[int, int, int]):
    # print(*state, sep="\n", end="\n\n")
    numW = len([cell for row in state for cell in row if cell == "W"])
    numB = len([cell for row in state for cell in row if cell == "B"])
    endings[:] = [endings[0] + int(numB > numW),
                  endings[1] + int(numW > numB),
                  endings[2] + int(numB == numW)]


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
