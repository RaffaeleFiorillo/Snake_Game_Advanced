# This module contains the functions responsible for the movement of the snake in the game. functions must check current
# state of the world and decide what is the next action of the snake. All functions have the same structure:
# - parameter: World object; - Return type: None; - Must use the "move_snake" method of the World class;

from game_entities import World
from random import random, choice
import pygame

DIRECTIONS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]


def keyboard_movement(world_i: World) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key in DIRECTIONS:
            world_i.move_snake(event.key)
            return None
    world_i.move_snake()


def random_movement(world_i: World) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if random() > 0.2:
        world_i.move_snake(choice(DIRECTIONS))


def hamiltonian_movement(world_i: World) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    right_points = ((0, 0) if i==0 else (1, i) for i in range(0, world_i.size, 2))
    left_points = ((world_i.size - 1, i) for i in range(1, world_i.size, 2))
    up_points = ((0, world_i.size - 1), )
    down_points = tuple((world_i.size - 1, i) for i in range(0, world_i.size, 2))
    down_points += tuple((1, i) for i in range(1, world_i.size-2, 2))
    snake_head = world_i.SNAKE.body_coordinates[0]
    direction = None
    if snake_head in right_points:
        direction = DIRECTIONS[1]
    elif snake_head in left_points:
        direction = DIRECTIONS[0]
    elif snake_head in down_points:
        direction = DIRECTIONS[3]
    elif snake_head in up_points:
        direction = DIRECTIONS[2]
    world_i.move_snake(direction)


def hamiltonian_simplified_movement(world_i: World) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    snake_head, direction = world_i.SNAKE.body_coordinates[0], None
    if snake_head == (0, 0) or (snake_head[0] == 1 and not snake_head[1] % 2):  # goes right
        direction = DIRECTIONS[1]
    elif snake_head[0] == world_i.size - 1 and snake_head[1] % 2:
        direction = DIRECTIONS[0]
    elif (snake_head[0] == world_i.size - 1 and not snake_head[1] % 2) or\
            (snake_head[0] == 1 and snake_head[1] % 2 and snake_head[1] != world_i.size-1):
        direction = DIRECTIONS[3]
    elif snake_head == (0, world_i.size - 1):
        direction = DIRECTIONS[2]
    world_i.move_snake(direction)

