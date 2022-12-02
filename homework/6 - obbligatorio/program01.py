#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Siete stati appena ingaggiati in una software house di videogiochi e
dovete renderizzare su immagine il giochino dello snake salvando
l'immagine finale del percorso dello snake e restituendo la lunghezza
dello snake.
Si implementi la funzione generate_snake che prende in ingresso un
percorso di un file immagine, che e' l'immagine di partenza
"start_img" che puo' contenere pixel di background neri, pixel di
ostacolo per lo snake di colore rosso e infine del cibo di colore
arancione. Lo snake deve essere disegnato di verde. Inoltre bisogna
disegnare in grigio la scia che lo snake lascia sul proprio
cammino. La funzione inoltre prende in ingresso una posizione iniziale
dello snake, "position" come una lista di due interi X e Y. I comandi
del giocatore su come muovere lo snake nel videogioco sono disponibili
in una stringa "commands".  La funzione deve salvare l'immagine finale
del cammino dello snake al percorso "out_img", che e' passato come
ultimo argomento di ingresso alla funzione. Inoltre la funzione deve
restituire la lunghezza dello snake al termine del gioco.

Ciascun comando in "commands" corrisponde ad un segno cardinale ed e
seguito da uno spazio. I segni cardinali possibli sono:

| NW | N | NE |
| W  |   | E  |
| SW | S | SE |

che corrispondono a movimenti dello snake di un pixel come:

| alto-sinistra  | alto  | alto-destra  |
| sinistra       |       | destra       |
| basso-sinistra | basso | basso-destra |

Lo snake si muove in base ai comandi passati e nel caso in cui
mangia del cibo si allunga di un pixel.

Lo snake puo' passare da parte a parte dell'immagine sia in
orizzontale che in verticale. Il gioco termina quando sono finiti i
comandi oppure lo snake muore. Lo snake muore quando:
- colpisce un ostacolo
- colpisce se stesso quindi non puo' passare sopra se stesso
- si incrocia in diagonale in qualsiasi modo. Ad esempio, un percorso
    1->2->3-4 come quello sotto a sinistra non e' lecito mentre quello a
    destra sotto va bene.

    NOT OK - diagonal cross        OK - not a diagonal cross
        | 4 | 2 |                    | 1 | 2 |
        | 1 | 3 |                    | 4 | 3 |

Ad esempio considerando il caso di test data/input_00.json
lo snake parte da "position": [12, 13] e riceve i comandi
"commands": "S W S W W W S W W N N W N N N N N W N"
genera l'immagine in visibile in data/expected_end_00.png
e restituisce 5 in quanto lo snake e' lungo 5 pixels alla
fine del gioco.

NOTA: analizzate le immagini per avere i valori esatti dei colore da usare.

NOTA: non importate o usate altre librerie
'''


import images


class HitObstacle(Exception):
    """Snaked stepped on an obstacle"""
    pass


class HitSelf(Exception):
    """Snaked stepped on itself"""
    pass


class Grid:
    colors = {
        "empty": (0, 0, 0),
        "obstacle": (255, 0, 0),
        "food": (255, 128, 0),
        "walked": (128, 128, 128),
        "snake": (0, 255, 0)
    }

    def __init__(self, snake, image: list[list[tuple[int, int, int]]]) -> None:
        self.snake: Snake = snake
        self.grid = image
        self.height = len(image)
        self.width = len(image[0])

    def toImg(self) -> list[list[tuple[int, int, int]]]:
        for pos in self.snake.pos:
            self.grid[pos["r"]][pos["c"]] = (0, 255, 0)
        return self.grid


class Snake:
    def __init__(self, position: dict[str, int]) -> None:
        self.pos = [position]
        self.color = (0, 255, 0)
        self.movements = {
            "N": self.__move_up,
            "S": self.__move_down,
            "E": self.__move_right,
            "W": self.__move_left,
            "NW": self.__move_up_left,
            "NE": self.__move_up_right,
            "SW": self.__move_down_left,
            "SE": self.__move_down_right
        }

    def move(self, movement: str, grid: Grid) -> None:
        self.__setWalked(grid)
        self.movements[movement](grid)
        self.__check_collision(grid)
        self.__check_grow(grid)

    def __move_up(self, grid: Grid):
        head = self.pos[0]
        if head["r"] == 0:
            self.pos.insert(0, {"r": grid.height - 1, "c": head["c"]})
        else:
            self.pos.insert(0, {"r": head["r"] - 1, "c": head["c"]})

    def __move_down(self, grid: Grid):
        head = self.pos[0]
        if head["r"] == grid.height - 1:
            self.pos.insert(0, {"r": 0, "c": head["c"]})
        else:
            self.pos.insert(0, {"r": head["r"] + 1, "c": head["c"]})

    def __move_right(self, grid: Grid):
        head = self.pos[0]
        if head["c"] == grid.width - 1:
            self.pos.insert(0, {"r": head["r"], "c": 0})
        else:
            self.pos.insert(0, {"r": head["r"], "c": head["c"]+1})

    def __move_left(self, grid: Grid):
        head = self.pos[0]
        if head["c"] == 0:
            self.pos.insert(0, {"r": head["r"], "c": grid.width-1})
        else:
            self.pos.insert(0, {"r": head["r"], "c": head["c"]-1})

    def __move_up_left(self, grid: Grid):
        head = self.pos[0]
        check = {"r": head["r"],
                 "c": head["c"]}
        if check["r"] == 0:
            check["r"] = grid.height - 1
        else:
            check["r"] -= 1
        if check["c"] == 0:
            check["c"] = grid.width - 1
        else:
            check["c"] -= 1
        self.__check_cross_collision(head, check)

    def __move_up_right(self, grid: Grid):
        head = self.pos[0]
        check = {"r": head["r"],
                 "c": head["c"]}
        if check["r"] == 0:
            check["r"] = grid.height - 1
        else:
            check["r"] -= 1
        if check["c"] == grid.width - 1:
            check["c"] = 0
        else:
            check["c"] += 1
        self.__check_cross_collision(head, check)

    def __move_down_left(self, grid: Grid):
        head = self.pos[0]
        check = {"r": head["r"],
                 "c": head["c"]}
        if check["r"] == grid.height - 1:
            check["r"] = 0
        else:
            check["r"] += 1
        if check["c"] == 0:
            check["c"] = grid.width - 1
        else:
            check["c"] -= 1
        self.__check_cross_collision(head, check)

    def __move_down_right(self, grid: Grid):
        head = self.pos[0]
        check = {"r": head["r"],
                 "c": head["c"]}
        if check["r"] == grid.height - 1:
            check["r"] = 0
        else:
            check["r"] += 1
        if check["c"] == grid.width - 1:
            check["c"] = 0
        else:
            check["c"] += 1
        self.__check_cross_collision(head, check)

    def __setWalked(self, grid: Grid):
        grid.grid[self.pos[-1]["r"]][self.pos[-1]["c"]] = Grid.colors["walked"]

    def __check_grow(self, grid: Grid):
        head = self.pos[0]
        cell = grid.grid[head["r"]][head["c"]]
        if cell != Grid.colors["food"]:
            self.pos.pop()

    def __check_collision(self, grid: Grid):
        head = self.pos[0]
        if grid.grid[head["r"]][head["c"]] == Grid.colors["obstacle"]:
            self.pos.pop(0)
            raise HitObstacle
        self.__check_self_collision()

    def __check_self_collision(self):
        head = self.pos[0]
        for pos in self.pos[1:]:
            if head == pos:
                self.pos.pop(0)
                raise HitSelf

    def __check_cross_collision(self, head, check):
        if {
            "r": head["r"],
            "c": check["c"]
        } in self.pos and {
            "r": check["r"],
            "c": head["c"]
        } in self.pos:
            raise HitSelf
        else:
            self.pos.insert(0, check)


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    image = images.load(start_img)

    snake = Snake({"r": position[1], "c": position[0]})

    grid = Grid(
        snake,
        image
    )

    movements = commands.split()
    try:
        for movement in movements:
            grid.snake.move(movement, grid)
    except HitObstacle:
        #print("hit obstacle")
        pass
    except HitSelf:
        #print("hit body")
        pass
    images.save(grid.toImg(), out_img)
    return len(grid.snake.pos)


if __name__ == "__main__":
    import time
    import json
    import os

    def get_input(input_json, key='input'):
        with open(input_json) as fr:
            js = json.load(fr)
            return js[key]

    start_time = time.time()
    for _i in range(11):
        zero = "0" if _i < 10 else ""
        print(f"test {zero}{_i}")
        data = get_input(f"./data/input_{zero}{_i}.json")
        image = images.load(data["start_img"])

        result = generate_snake(
            start_img=data["start_img"],
            position=data["position"],
            commands=data["commands"],
            out_img=data["out_img"].replace(
                "/output/output_end_", "/test/test")
        )
        # print(grid.toImg())
        print(f"snake lenght: {result}")
        print("-"*os.get_terminal_size().columns)

    print(f'Execution time: {time.time() - start_time}s')
