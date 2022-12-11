#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images

from line_profiler_pycharm import profile


class HitObstacle(Exception):
    """Snaked stepped on an obstacle"""
    pass


class HitSelf(Exception):
    """Snaked stepped on itself"""
    pass

@profile
def move_up(snake_positions, img):

    head = snake_positions[0]
    new_pos = [head[0]-1, head[1]]
    if new_pos[0] == -1:
        new_pos[0] = len(img)-1
    snake_positions.insert(0, new_pos)


def move_down(snake_positions, img):
    head = snake_positions[0]
    new_pos = [head[0]+1, head[1]]
    if new_pos[0] == len(img):
        new_pos[0] = 0
    snake_positions.insert(0, new_pos)

@profile
def move_left(snake_positions, img):
    head = snake_positions[0]
    new_pos = [head[0], head[1]-1]
    if new_pos[1] == -1:
        new_pos[1] = len(img[0])-1
    snake_positions.insert(0, new_pos)

@profile
def move_right(snake_positions, img):
    head = snake_positions[0]
    new_pos = [head[0], head[1]+1]
    if new_pos[1] == len(img[0]):
        new_pos[1] = 0
    snake_positions.insert(0, new_pos)

@profile
def move_up_left(snake_positions, img):
    head = snake_positions[0]
    new_pos = [head[0]-1, head[1]-1]
    if new_pos[0] == -1:
        new_pos[0] = len(img)-1
    if new_pos[1] == -1:
        new_pos[1] = len(img[0])-1
    snake_positions.insert(0, new_pos)

@profile
def move_up_right(snake_positions, img):
    head = snake_positions[0]
    new_pos = [head[0]-1, head[1]+1]
    if new_pos[0] == -1:
        new_pos[0] = len(img)-1
    if new_pos[1] == len(img[0]):
        new_pos[1] = 0
    snake_positions.insert(0, new_pos)

@profile
def move_down_left(snake_positions, img):
    head = snake_positions[0]
    new_pos = [head[0]+1, head[1]-1]
    if new_pos[0] == len(img):
        new_pos[0] = 0
    if new_pos[1] == -1:
        new_pos[1] = len(img[0])-1
    snake_positions.insert(0, new_pos)

@profile
def move_down_right(snake_positions, img):
    head = snake_positions[0]
    new_pos = [head[0]+1, head[1]+1]
    if new_pos[0] == len(img):
        new_pos[0] = 0
    if new_pos[1] == len(img[0]):
        new_pos[1] = 0
    snake_positions.insert(0, new_pos)


def get_img(img):
    return images.load(img)

@profile
def move_snake(img, snake_positions, movement, colors):
    movements = {
        "N": move_up,
        "S": move_down,
        "E": move_right,
        "W": move_left,
        "NW": move_up_left,
        "NE": move_up_right,
        "SW": move_down_left,
        "SE": move_down_right
    }
    head = snake_positions[0]
    top, bottom, left, right = cross(img, head)
    #debug_cross(img, colors, top, bottom, left, right)
    movements[movement](snake_positions, img)
    head = check_hit(img, snake_positions, colors)

    if movement in {"NE", "NW", "SE", "SW"}:
        check_cross_hit(movement, top, bottom, left, right, snake_positions)

    check_food(img, snake_positions, colors, head)

@profile
def cross(img, head):
    top = [len(img)-1 if head[0] == 0 else head[0]-1, head[1]]
    bottom = [0 if head[0] == len(img) else head[0]+1, head[1]]
    left = [head[0], len(img[0])-1 if head[1] == 0 else head[1]-1]
    right = [head[0], 0 if head[1] == len(img[0])-1 else head[1]+1]

    return top, bottom, left, right

@profile
def check_food(img, snake_positions, colors, head):
    did_eat: bool = img[head[0]][head[1]] == colors["food"]
    img[head[0]][head[1]] = colors["snake"]
    if not did_eat:
        tail = snake_positions[-1]
        img[tail[0]][tail[1]] = colors["walked"]
        snake_positions.remove(tail)

@profile
def check_cross_hit(movement, top, bottom, left, right, snake_positions):
    cross_dict = {
        "NW": check_cross_hit_NW,
        "NE": check_cross_hit_NE,
        "SW": check_cross_hit_SW,
        "SE": check_cross_hit_SE
    }
    cross_dict[movement](top, bottom, left, right, snake_positions)

@profile
def check_cross_hit_NW(top, bottom, left, right, snake_positions):
    if top in snake_positions and left in snake_positions:
        snake_positions.pop(0)
        raise HitSelf

@profile
def check_cross_hit_NE(top, bottom, left, right, snake_positions):
    if top in snake_positions and right in snake_positions:
        snake_positions.pop(0)
        raise HitSelf

@profile
def check_cross_hit_SW(top, bottom, left, right, snake_positions):
    if bottom in snake_positions and left in snake_positions:
        snake_positions.pop(0)
        raise HitSelf

@profile
def check_cross_hit_SE(top, bottom, left, right, snake_positions):
    if bottom in snake_positions and right in snake_positions:
        snake_positions.pop(0)
        raise HitSelf

@profile
def check_hit(img, snake_positions, colors):
    head = snake_positions[0]
    if img[head[0]][head[1]] == colors["snake"]:
        snake_positions.pop(0)
        raise HitSelf
    elif img[head[0]][head[1]] == colors["obstacle"]:
        snake_positions.pop(0)
        raise HitObstacle
    return head


def debug_cross(img, colors, top, bottom, left, right):
    img[top[0]][top[1]] = colors["debug"]
    img[bottom[0]][bottom[1]] = colors["debug"]
    img[left[0]][left[1]] = colors["debug"]
    img[right[0]][right[1]] = colors["debug"]

@profile
def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    # sourcery skip: use-contextlib-suppress

    colors = {
        "empty": (0, 0, 0),
        "obstacle": (255, 0, 0),
        "food": (255, 128, 0),
        "walked": (128, 128, 128),
        "snake": (0, 255, 0),
        "debug": (0, 0, 255)
    }

    # noinspection PyShadowingNames
    image = get_img(start_img)
    snake_positions = [[position[1], position[0]]]

    image[position[1]][position[0]] = colors["snake"]

    try:
        for movement in commands.split():
            # print(movement)
            move_snake(img=image, snake_positions=snake_positions,
                       movement=movement, colors=colors)
    except (HitObstacle, HitSelf):
        pass

    images.save(img=image, filename=out_img)
    return len(snake_positions)


if __name__ == "__main__":
    import json
    import time
    # noinspection PyUnresolvedReferences
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
            #commands="N ".replace("N", "SE")*15,
            #commands="N N W NW E NE SE E E E S S SE E NW SW",
            out_img=data["out_img"].replace(
                "/output/output_end_", "/test/test")
        )
        # print(grid.toImg())
        print(f"snake length: {result}")
        #print("-"*os.get_terminal_size().columns)

    print(f'Execution time: {time.time() - start_time}s')
