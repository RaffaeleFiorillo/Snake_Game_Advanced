import pygame
import movement_functions as mf
import game_entities as ge
import time


def test_speed(funct, lable):
    print(lable)
    times, iterations = [], 10000
    world_i = ge.World(SCREEN, WORLD_SIZE, CELL_SIZE)
    for i in range(iterations):
        t1 = time.time()
        funct(world_i)
        t2 = time.time()
        times.append(t2-t1)
    print(f"Time of execution ({iterations}x): {sum(times)} | Average time/iteration: {sum(times)/iterations}\n")


def test_speed_2():
    world_i = ge.World(SCREEN, WORLD_SIZE, CELL_SIZE)
    times, iterations = [], 10000
    for i in range(iterations):
        t1 = time.time()
        right_points = ((0, 0) if i==0 else (1, i) for i in range(0, world_i.size, 2))
        left_points = ((world_i.size - 1, i) for i in range(1, world_i.size, 2))
        up_points = ((0, world_i.size - 1), )
        down_points = tuple((world_i.size - 1, i) for i in range(0, world_i.size, 2))
        down_points += tuple((1, i) for i in range(1, world_i.size-2, 2))
        t2 = time.time()
        times.append(t2-t1)
    print(f"Time of execution ({iterations}x): {sum(times)} | Average time/iteration: {sum(times)/iterations}\n")


pygame.init()
pygame.font.init()
WORLD_SIZE = 24
CELL_SIZE = 20
SCREEN = pygame.display.set_mode((WORLD_SIZE*CELL_SIZE, WORLD_SIZE*CELL_SIZE))
CLOCK = pygame.time.Clock()
TEXT_FONT = pygame.font.SysFont('Times New Roman', 12)

"""test_speed(mf.hamiltonian_movement, "Normal Version:\n")   # 0.15226244926452637 total time 10000
test_speed(mf.hamiltonian_movement_simplified, "Simplified Version:\n")""" # 0.028067350387573242 total time 10000

test_speed_2()  # 0.11562085151672363 total time

print(0.15226244926452637 - 0.11562085151672363)
